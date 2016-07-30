from django.db import models

class Author(models.Model):
  name = models.CharField(max_length=100)
  password = models.CharField(max_length=100)
  age = models.IntegerField(default=0)

  def __str__(self):
    return self.name

class Book(models.Model):
  author = models.ForeignKey(Author, on_delete = models.CASCADE)
  name = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

  def __str__(self):
    return self.name

