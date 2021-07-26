from django.urls import path
from . import views

app_name = "wishlist"

urlpatterns = [
    path('', views.wishlist_summary, name='wishlist_summary'),
    path('add/', views.wishlist_add, name='wishlist_add'),
    path('delete/', views.wishlist_delete, name='wishlist_delete'),
    # path('update/', views.wishlist_update, name='wishlist_update'),
]
