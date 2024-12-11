from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.


class Coffee(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()
    quantity=models.IntegerField()
    image=models.CharField(max_length=2083)
    # def __str__(self):
    #     return f"{self.name}  "

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    #image = models.ImageField(upload_to="posts",null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(db_index=True , unique=True)
    content = models.TextField(validators= [MinLengthValidator(10)])