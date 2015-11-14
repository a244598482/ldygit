from django.db import models
class Author(models.Model):
	AuthorID = models.CharField(max_length=5)
	Name = models.CharField(max_length=10)
 	Age = models.CharField(max_length=3)
	Countury = models.CharField(max_length=10)
class Book(models.Model):
	ISBN = models.CharField(max_length=7)
	Title = models.CharField(max_length=12)
	AuthorID = models.ForeignKey(Author)
	Publisher = models.CharField(max_length=20)
	PublishDate = models.CharField(max_length=15)
	Price = models.CharField(max_length=3)

