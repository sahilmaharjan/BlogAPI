from django.db import models
from accounts.models import User

class Categories(models.Model):
    name = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank= False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.TextField(null=False, blank=False)
    # categories  = models.ForeignKey(Categories, models.SET_NULL,
    # blank=True,
    # null=True,)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title