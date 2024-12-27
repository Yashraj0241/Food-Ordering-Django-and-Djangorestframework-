# Food Ordering App

## **About the Project**
The **Food Ordering App** is a web-based application developed using Django and Django REST Framework (DRF). It provides a seamless user experience for browsing restaurants, viewing menus, managing a cart, and placing orders with multiple payment options. The application is fully API-driven, and tools like **Postman** have been used to test and verify the API endpoints.

---

## **Table of Contents**
- [About the Project](#about-the-project)
- [Features](#features)
- [Workflow](#workflow)
- [Technologies Used](#technologies-used)
- [Database Models](#database-models)
- [Setup and Installation](#setup-and-installation)
- [API Testing with Postman](#api-testing-with-postman)
- [Usage](#usage)

---

## **Features**
- **User Authentication:**
  - User registration and login functionality.
  - Redirects users to the registration page if they attempt to log in without registering.
- **Restaurant Browsing:**
  - Displays a list of restaurants with details like name, rating, and location.
- **Menu Viewing:**
  - Dedicated restaurant page with its menu, item details, and an "Add to Cart" option.
- **Cart Management:**
  - Add multiple items to the cart and view their details, including price and quantity.
  - Remove specific items from the cart.
  - Displays total bill amount.
- **Order Placement:**
  - Supports multiple payment methods like Google Pay, PhonePe, and Cash on Delivery.
  - Displays an order confirmation page with order details and a thank-you message.
- **Navigation:**
  - Easy navigation between pages, including a "Back to Restaurant" option.

---

## **Workflow**

1. **User Registration and Login:**
   - New users must register before accessing the app.
   - Attempting to log in without registering redirects users to the registration page.
2. **Restaurant Listing:**
   - After login, users are redirected to the restaurant list page.
   - Each restaurant displays its name, rating, and location.
3. **Menu Viewing:**
   - Clicking on a restaurant leads to its dedicated menu page.
   - Users can add items to their cart from this page.
4. **Cart Management:**
   - Users can view their cart, modify quantities, and remove items.
   - The total bill is displayed with a "Proceed to Payment" button.
5. **Order Placement:**
   - Users select a payment method and confirm the order.
   - The order confirmation page displays order details and a thank-you message.

---

## **Technologies Used**

- **Backend:**
  - Django
  - Django REST Framework (DRF)
  - SQLite
- **Frontend:**
  - HTML
  - CSS (inline styles and Bootstrap)
  - JavaScript
- **Tools:**
  - **Postman**: For API endpoint testing and validation.
  - Django Admin for authentication management
  - Virtual environment for dependency management

---

## **Database Models**

python
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


## **API Testing with Postman**

You can use Postman to test the API endpoints of the Food Ordering App.

### **Base URL:**
The base URL for the API is `http://127.0.0.1:8000/api/`.

### **Available Endpoints:**

#### **User Authentication:**
- `POST /api/register/`: Register a new user.
- `POST /api/login/`: Log in an existing user.

#### **Restaurant Endpoints:**
- `GET /api/restaurants/`: Get the list of all restaurants.
- `GET /api/restaurants/{id}/`: Get details of a specific restaurant.

#### **Menu Endpoints:**
- `GET /api/menu/{restaurant_id}/`: Get the menu for a specific restaurant.

#### **Cart Endpoints:**
- `GET /api/cart/`: Get the current user's cart.
- `POST /api/cart/add/`: Add an item to the cart.
- `DELETE /api/cart/remove/`: Remove an item from the cart.

#### **Order Endpoints:**
- `POST /api/order/`: Place an order.

### **Testing API Endpoints:**
Use Postman to send requests to these endpoints. Ensure that you pass the necessary authentication headers (e.g., `Authorization: Token <your_token>` for authenticated requests).
