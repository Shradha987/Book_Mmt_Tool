from django.contrib import admin
from books.models import *
# Register your models here.
admin.site.register(Books)
admin.site.register(Genre)