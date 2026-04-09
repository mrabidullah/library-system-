from django.contrib import admin
from app1.models import book_s
from .models import books_issues,comment

# Register your models here.
@admin.register(book_s)
class book_a(admin.ModelAdmin):
    list_display=['books_name','books_title','books_author','books_descripation','media']
    
    
#======================BOOK_issues______________________________>

@admin.register(books_issues)
class book_iss(admin.ModelAdmin):
    sreach_Filed=['name','books_name','phone_no']
    l=['issue_time']
    
    
#___________the comment section______________________________________>
@admin.register(comment)
class comt(admin.ModelAdmin):
    list_display=['comment1','user']
    a=[' created_at']
    
