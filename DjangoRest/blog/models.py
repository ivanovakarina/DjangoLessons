from django.db import models
from django.db.models import CharField, TextField, DateTimeField, ImageField

# Create your models here.
class Post(models.Model):
    title = CharField(max_length=100)
    text = TextField()
    image = ImageField(upload_to='images/%Y/%m/%d')
    create_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self): #переопределили что-то, чтобы не было абракадабры
        return self.title

