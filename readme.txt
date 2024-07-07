# Ecommerce Website

This is an ecommerce website built with Django. This README file provides instructions on setting up the project on your local machine for development and testing purposes.

## Table of Contents

- [Installation](#installation)
- [Database Setup](#database-setup)
- [Running the Server](#running-the-server)
- [Testing Accounts](#testing-accounts)
- [Project Structure](#project-structure)
- [Features](#features)
- [Contributing](#contributing)

## Installation

1. *Clone the repository*:
    bash
    git clone https://github.com/Qambar-12/Ecommerce-Website
    cd ecommerce-website
    cd Almari
    

2. *Create a virtual environment*:
    bash/cmd/powershell
    python -m venv venv
    

3. *Activate the virtual environment*:
    - On Windows:
        bash/cmd/powershell
        venv\Scripts\activate
        
    - On MacOS/Linux:
        bash/cmd/powershell
        source venv/bin/activate
        

4. *Install the required packages*:
    bash/cmd/powershell
    pip install django
    pip install pillow
    pip install django-environ
    

## Database Setup

1. *Make migrations*:
    bash/cmd/powershell
    python manage.py makemigrations
    

2. *Apply migrations*:
    bash/cmd/powershell
    python manage.py migrate
    

## Running the Server

1. *Start the development server*:
    bash/cmd/powershell
    python manage.py runserver
    

2. Open your web browser and go to http://127.0.0.1:8000 to see the website in action.

## Testing Accounts

Here are some pre-created accounts for testing purposes:

### Administrator Account
    - *Username*: drmaria
    - *Password*: bateinNaKarein*

### Customer Accounts
Create customer account by signing up on our website make sure to use a valid "Email" so that you can receive a verification code to confirm order
    *Demo Accounts*
    - *Username*: Qambar
    - *Password*: 1234567*

    - *Username*: asad123
    - *Password*: as@d1234

## Project Structure

A brief overview of the project's structure:


ecommerce-website/
└──Almari
    │
    ├── Almari/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   ├── asgi.py
    │   └── OOP/
    |        └── ...
    |
    ├── cart/checkout/store/user/
    │   ├── migrations/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    │
    ├── templates/
    │   ├── base.html
    │   ├── index.html
    │   └── ...
    │
    ├── static/
    │   ├── css/
    │   ├── js/
    │   └── images/
    │
    └──manage.py

For every app in a django project these 3 files are necessary
1. urls.py
2. views.py
3. templates

## Features

- *User Authentication*: Secure login and registration for customers and administrators.
- *Product Management*: Add, edit, and delete products.
- *Shopping Cart*: Add products to the cart and proceed to checkout.
- *Order Management*: View and manage orders.
- *Search Functionality*: Search for products by name or category.

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -am 'Add new feature').
5. Push to the branch (git push origin feature-branch).
6. Create a new Pull Request.
