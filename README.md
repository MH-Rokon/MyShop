# EcomWeb - Phone Selling Platform

An e-commerce web application focused on selling mobile phones. Built with Django for the backend and Bootstrap for the frontend, featuring product listings, user authentication, and a shopping cart system.

## Features

- User registration and login
- Browse and search mobile phone products
- Product detail pages with images and descriptions
- Add to cart and checkout functionality
- Responsive design with Bootstrap
- Admin panel for product management

## Technologies Used

- Python, Django
- HTML, CSS, Bootstrap
- PostgreSQL (or your database)
- Deployed on Render.com (or specify your deployment)

## Setup Instructions

```bash
git clone https://github.com/MH-Rokon/MyShop.git
cd ecomweb-phone-selling
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
