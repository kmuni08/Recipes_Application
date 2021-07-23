from .models import Category

def categories(request):
    # print("categories", Category.objects.all())
    return {
        'categories': Category.objects.all()
    }