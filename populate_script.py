"""This script will fill data base with a superuser, 10 categories, 10 contractors and 50 products. Superuser username
will be 'admin' and password will be 'password'. Run this script after migrations if you are using other database
than this in this project.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FPPlite.settings')
django.setup()

from django.contrib.auth.models import User
from FPP.models import Category, Contractor, ProductHistory, Product
from faker import Faker
import random


def create_superuser():
    superuser = User.objects.create_superuser('admin', 'admin@admin.com', 'password')
    superuser.save()


def create_categories():
    faker = Faker()
    for _ in range(10):
        category = faker.word(ext_word_list=None)
        Category.objects.create(category=category)


def create_contractors():
    faker = Faker()
    for _ in range(10):
        type = random.randint(1, 2)
        name = faker.first_name() + " " + faker.last_name()
        contact = faker.street_name() + " " + faker.email() + " " + faker.phone_number()
        Contractor.objects.create(type=type, name=name, contact=contact)


def create_products():
    faker = Faker()
    for _ in range(50):
        new_product = Product.objects.create(code=faker.random_int(min=1000, max=9999),
                                             name=faker.word(ext_word_list=None),
                                             quantity=faker.random_int(min=1000, max=9999),
                                             description=faker.sentence(nb_words=6, variable_nb_words=True,
                                                                        ext_word_list=None),
                                             category=Category.objects.get(id=random.randint(1, 10)))
        new_price = ProductHistory.objects.create(purchase_price=50,
                                                  price_for_sale=99.99)
        new_product.price_for_sale.add(new_price)
        new_product.save()


create_superuser()
create_categories()
create_contractors()
create_products()
