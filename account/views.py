from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

# from orders.views import user_orders
from recipe.models import Recipe
from .forms import RegistrationForm, UserEditForm
from .models import UserBase
from .tokens import account_activation_token


@login_required
def dashboard(request):
    return render(request, 'account/user/dashboard.html')

@login_required
def wishlist(request):
    recipes = Recipe.objects.filter(users_wishlist = request.user)
    return render(request, 'account/user/user_wishlist.html', {"wishlist": recipes})

@login_required
def add_to_wishlist(request,id):
    recipe = get_object_or_404(Recipe, id=id)
    if recipe.users_wishlist.filter(id=request.user.id).exists():
        recipe.users_wishlist.remove(request.user)
        messages.success(request, recipe.title + " has been removed from your WishList. ")
    else:
        recipe.users_wishlist.add(request.user)
        messages.success(request, "Added " + recipe.title + " to your WishList.")
    return HttpResponseRedirect(request.META["HTTP_REFERER"])



@login_required
def edit_details(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)

        if user_form.is_valid():
            user_form.save()
            print("user_form is valid", {'user_form': user_form})
    else:
        user_form = UserEditForm(instance=request.user)
        print("user_form in else", {'user_form': user_form})
        

    return render(request,'account/user/edit_details.html', {'user_form': user_form})


@login_required
def delete_user(request):
    user = UserBase.objects.get(user_name=request.user)
    user.is_active = False
    user.save()
    logout(request)
    return redirect('account:delete_confirmation')


def account_register(request):

    if request.user.is_authenticated:
        return redirect('account:dashboard')

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('account/registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)
            return HttpResponse('registered succesfully and activation sent')
    else:
        registerForm = RegistrationForm()
    return render(request, 'account/registration/register.html', {'form': registerForm})


def account_activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('account:dashboard')
    else:
        return render(request, 'account/registration/activation_invalid.html')
