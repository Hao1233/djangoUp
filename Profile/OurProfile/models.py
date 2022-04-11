from itertools import count
from statistics import mode
import django
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Customer(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Post(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    images = models.ImageField(null = True,blank=True)
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Tag,null=True)
    public = models.BooleanField(default=False)
    private = models.BooleanField(default=False)
    slug = models.SlugField(null = True,blank=True)
    def __str__(self):
        return self.title
    
    
    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.title)

            has_slug = Post.objects.filter(slug=slug).exists()
            counts = 1
            while has_slug:
                counts +=1
                slug = slugify(self.title) + '-' + str(counts)
                has_slug = Post.objects.filter(slug=slug).exists()
        self.slug = slug
        super().save(*args,**kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    customer_comment = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.body