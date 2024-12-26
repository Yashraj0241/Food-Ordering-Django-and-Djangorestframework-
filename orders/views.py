# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect , get_object_or_404    #  rendering templates and return http response
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required         # its used for only authenticated users access it
from .models import Restaurant,Menu,Cart,CartItem
from django.urls import reverse                   # generate URL from the name of URL pattern


# Registration Page
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')

    return render(request, 'register.html')

# Login Page
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)       # if success then it(user object) holds all details of User model otherwise None
        if user is not None:
            login(request, user)
            return redirect('restaurant_list')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'login.html')




@login_required
def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant_list.html', {'restaurants': restaurants})





@login_required
def restaurant_menu(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)   # retrives object from database based on given query
    menu_items = Menu.objects.filter(restaurant=restaurant)
    return render(request, 'restaurant_menu.html', {'restaurant': restaurant, 'menu_items': menu_items})




from django.http import JsonResponse

@login_required
def add_to_cart(request, item_id):
    menu_item = get_object_or_404(Menu, id=item_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, menu_item=menu_item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return JsonResponse({"message": "Item added to cart!"})


@login_required
def view_cart(request):
    # item={}
    try:
        # Fetch the cart for the current user
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        total_price = sum(item.menu_item.price * item.quantity for item in cart_items)
        #for item in cart_items:
        #    item['total_price'] = item['menu_item']['price'] * item['quantity']
    except Cart.DoesNotExist:
        cart_items = []
        total_price = 0

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        "items" : cart_items

    })




@login_required
def remove_from_cart(request, item_id):
    try:
        cart_item = CartItem.objects.get(id=item_id, cart__user=request.user)
        cart_item.delete()
        messages.success(request, "Item removed from cart.")
    except CartItem.DoesNotExist:
        messages.error(request, "Item not found in your cart.")
    return redirect('cart')




@login_required
def payment_methods(request):
    if request.method == "POST":
        selected_method = request.POST.get("payment_method")
        if not selected_method:
            messages.error(request, "Please select a payment method.")
            return redirect('payment')

        # Redirect to the final order page
        return redirect(reverse('final_order', kwargs={'payment_method': selected_method}))

    return render(request, 'payment_methods.html')






@login_required
def final_order(request, payment_method):
    try:
        cart = Cart.objects.get(user=request.user)
        items = cart.cartitem_set.all()
        total_price = sum(item.menu_item.price * item.quantity for item in items)
    except Cart.DoesNotExist:
        items = []
        total_price = 0

    return render(request, 'final_order.html', {
        'items': items,
        'total_price': total_price,
        'payment_method': payment_method,
    })
