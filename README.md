content = """# Food Ordering App

## Overview
The **Food Ordering App** is a web-based application built using Django and Django REST Framework. It provides users with an intuitive interface to browse restaurants, view their menus, add items to a cart, and place orders with multiple payment options. The app ensures a seamless user experience with authentication mechanisms and robust backend functionalities.

## Features
- **User Authentication:**
  - User registration and login functionality.
  - Redirects users to the registration page if they attempt to log in without an account.
- **Restaurant Browsing:**
  - Displays a list of restaurants with their names, ratings, and locations.
- **Menu Viewing:**
  - Each restaurant has a dedicated page showing its menu with item names, prices, and an option to add items to the cart.
- **Cart Management:**
  - Users can add multiple items to the cart.
  - View added items, their prices, quantities, and the total bill in the cart.
  - Option to remove items from the cart.
- **Order Placement:**
  - Multiple payment methods like Google Pay, PhonePe, and Cash on Delivery.
  - Order confirmation page showing order details and a "Thank you" message.
- **Navigation:**
  - Easy navigation back to the restaurant list page after placing an order.

## Workflow
1. **User Registration and Login:**
   - New users must register to access the app.
   - Registered users can log in and access the restaurant list.
   - Attempting to log in without registration redirects to the registration page.
2. **Restaurant Listing:**
   - After login, users are directed to the restaurant list page.
   - Each restaurant entry shows its name, rating, and location.
3. **Menu Browsing:**
   - Clicking on a restaurant shows its menu.
   - Menu items include the name, price, and an "Add to Cart" button.
4. **Cart Management:**
   - Items can be added to the cart.
   - Users can view, modify, and remove items from the cart.
   - Total bill is displayed with a "Proceed to Payment" option.
5. **Order Placement:**
   - Users select a payment method and confirm the order.
   - The order confirmation page displays the order summary, total price, and a thank-you message.
   - Users can navigate back to the restaurant list page.

## Technologies Used
### Backend:
- **Django:** Framework for building the application.
- **Django REST Framework:** For handling RESTful operations.
- **SQLite:** Database for storing application data.

### Frontend:
- **HTML:** For structuring the pages.
- **CSS & Bootstrap:** For styling and responsive design.
- **JavaScript:** For interactivity.

### Authentication:
- **Django's User Model:** Predefined model for user authentication (login, logout, registration).

## Database Models
```python
from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    rating = models.FloatField()

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

