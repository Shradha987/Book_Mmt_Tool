from django.db import models

class Genre(models.Model):
   GenreId = models.AutoField(primary_key=True)
   GenreName = models.CharField(max_length=100)

# Create your models here.
class Books(models.Model):
    book_title = models.CharField(max_length=30,null = False)
    author = models.CharField(max_length=20)
    genre_of_book = models.CharField(max_length=100)
    type_of_book = models.CharField(max_length=100)
    publication = models.CharField(max_length=20)
    number_of_pages = models.IntegerField()
    price_of_book = models.FloatField()
    cover_of_book = models.ImageField(default='NA',upload_to='static/books/cover_photo/')


    class Meta:
        db_table = 'Books_Master'