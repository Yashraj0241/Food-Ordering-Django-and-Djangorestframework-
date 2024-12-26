from django.urls import path
from .views import register, login_view , restaurant_list , restaurant_menu , add_to_cart, view_cart, remove_from_cart , payment_methods , final_order

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('restaurants/', restaurant_list, name='restaurant_list'),
    path('restaurants/<int:restaurant_id>/menu/', restaurant_menu, name='restaurant_menu'),
    path('cart/add/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='cart'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('payment/', payment_methods, name='payment'),
    path('final_order/<str:payment_method>/', final_order, name='final_order'),
]





