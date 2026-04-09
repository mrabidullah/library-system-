from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class book_s(models.Model):
    books_name=models.CharField(max_length=50,null=True)
    books_title=models.CharField(max_length=50,null=True)
    books_author=models.CharField(max_length=50,null=True)
    books_descripation=models.TextField()
    media=models.ImageField(upload_to='image',max_length=250,null=False)
    
    def __str__(self):
        return self.books_name
    
    
#=================================================  BOOKS ISSUES  ======================>


class books_issues(models.Model):
    
    name=models.CharField(max_length=50,null=True)
    books_name=models.CharField(max_length=50,null=True)
    phon_no=models.IntegerField(unique=True)
    issue_time=models.DateTimeField(auto_now_add=True)
    
    
    
#_______________the comment section  ________________________________________________________>
class comment(models.Model):
    comment1=models.TextField(null=True)
    
    book_ss=models.ForeignKey(book_s,on_delete=models.CASCADE,null=True)
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.comment1