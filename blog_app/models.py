
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
# class UsersList(models.Model):

    # # Username=models.CharField(max_length=100)
    # email=models.AutoField(primary_key=True)
    # password= models.CharField(max_length = 150)
    # phone_no=models.CharField(max_length=100)
    
class BlogList(models.Model):

    Blog_title=models.CharField(max_length=200)
    Author_name=models.CharField(max_length=200)
    Published_date=models.DateField()
    Blog_detail=models.CharField(max_length=1000)
    Blog_image=models.ImageField(upload_to="blogs")

    BLOG_CATEGORIES=[  
        ('option1', 'Business'),
        ('option2', 'Culture'),
        ('option3', 'Food'),
        ('option4','Technology'),
        ('option4','Social'),
    ]
    Blog_category=models.CharField(max_length=500,choices=BLOG_CATEGORIES,default='option4',null=True,blank=True)


class BlogPost(models.Model):
    Blog_likes=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='liked_posts')
    
    def total_likes(self):
        return self.likes.count()