from Book.models import Book
from django.contrib.auth.models import User


# exec(open(r'F:\Python(Rohit)\Django_projects\Libraryproject\Book\db_shell.py').read())

# custom model manager:-

# print(Book.objects.get_active_objects()) 

# print(Book.objects.get_inactive_objects())

# print(Book.objects.all())

# print(Book.objects.using("secondry").all())   # get record in secondry database table

# ---------------



# create data from backend:-

# from datetime import datetime 
# Book.objects.using("secondry").create(title = "Book7", author = "auth7", publication_date = datetime(2022, 8, 18), price = "270")

# -------------------
 

# Custom command:- (create own command for our aplication)

# create user:-

# User.objects.create_user(username="lajari", email="lajari@gmail.com", password="Lajari@123")

# User.objects.create_user(username="saurabh", email="saurabh@gmail.com", password="Saurabh@123")

# print(User.objects.all())    # check user


# --------------------

# create super_user:-

# User.objects.create_superuser(username="ayush", email="ayush@gmail.com", password="Ayush@123")

# print(User.objects.all())    # check user

# ---------------------------



