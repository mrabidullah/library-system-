from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from app1.models import book_s,books_issues,comment
from django.shortcuts import get_object_or_404

# Create your views here.

def usersignup(request):
    c=''
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        
        if pass1!=pass2:
            c='your password wrong try again'
        else:
            user=User.objects.create_user(name,email,pass1)
            user.save()
            return redirect('login')
    return render(request,'signup.html',{'c':c})

#________________  LOGIN   ____________________________________________________>

def userlogin(request):
    if request.method=='POST':
        name=request.POST.get('password')
        pass1=request.POST.get('username')
        
        user=authenticate(username=name,password=pass1)
        if user is not None:
            login(request,user)
        return redirect('home')
    return render(request,'login.html')    

def home(request):
    return render(request,'home.html')



def books(request):
    data=book_s.objects.all()
    
    return render(request,'books.html',{'data':data})

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?

def books_issue(request):
    books_issue=books_issues.objects.all()
    if request.method=='POST':
        name=request.POST.get('search')
        if name!=None:
            books_issue=books_issues.objects.filter(name__icontains=name)
        
    return render(request,'book_issue.html',{"issue":books_issue})

#____________________________________________________________________________________________?



def book_form(request, id):
    data = get_object_or_404(book_s, id=id)
    a = comment.objects.filter(book_ss=data)
    book_error = ''

    if request.method == 'POST':
        name = request.POST.get('name')
        book = request.POST.get('books_name')
        phone = request.POST.get('phon_no')
        time = request.POST.get('sent_time')
        coment=request.POST.get('comment1')
        if request.user.is_authenticated:
            comment.objects.create(book_ss=data, comment1=coment, user=request.user)



        # ✅ Replace data.title with your actual book field name (maybe title, book_name, etc.)
        
            if book.strip().lower() != data.books_name.strip().lower():
                book_error = '❌ Book name does not match!'
            else:
               form = books_issues(
                name=name,
                books_name=book,
                phon_no=phone,
                issue_time=time,
                )
               form.save()
            return redirect('form',id=id)

    return render(request, 'book_form.html', {
        'i': data,
        'a': a,
        'book_error': book_error
    })


def book_form1(request):
  
    return render(request,'form.html')




#_________________the first models work and form front to backend data _______________::::


def first_models_form(request):
    i=book_s.objects.all()
    if request.method=='POST':
        book_name=request.POST.get('books_name')
        book_title=request.POST.get('books_title')
        book_description=request.POST.get('books_description')
        book_author=request.POST.get('books_author')
        media=request.FILES.get('media')
        # if all([book_name, book_title, book_description, book_author, media]):
        data=book_s(
            books_name=book_name,
            books_title=book_title,
            books_descripation=book_description,
            books_author=book_author,
            media=media,
        )
        data.save()
        return redirect('admin')
    return render(request,'form.html')








#___________admin section ______________________________>

def adminabid(request):
    data1=book_s.objects.all()
    data2=books_issues.objects.all()
    data3=comment.objects.all()
    
    return render(request,'admin.html',{'data1':data1,'data2':data2,'data3':data3})



def adminlogin(request):
    error=''
    name="Abid"
    password4='123abid'
    if request.method=='POST':
        name1=request.POST.get('name')
        passadmin=request.POST.get('password3')
        
        if name !=name1 and password4 !=passadmin:
           error='your password is not match try again'
            
        else:
            
            return redirect('admin')
    return render(request,'adminlogin.html',{'error':error})



def admin_search(request):
    data1=book_s.objects.all()
    if request.method=='POST':
        srch=request.POST.get('search')
        if srch !=None:
            data1=book_s.objects.filter(books_name__icontains=srch)
        
    return render(request,'admin.html',{'data1':data1})







#____________ admin search _____________________________________________________?
def admin_delete(request,id):
    delete=book_s.objects.filter(id=id)
    delete.delete()
    delete1=books_issues.objects.filter(id=id)
    delete1.delete()
    delete2=comment.objects.filter(id=id)
    delete2.delete()
    return redirect('admin')




def admin_update(request,id):
    update=book_s.objects.get(id=id)
    if request.method=='POST':
           update.books_name=request.POST.get('books_name')
           update.books_title=request.POST.get('books_title')
           update.books_author=request.POST.get('books_author')
           update.books_descripation=request.POST.get('books_description')
       
           media=request.FILES.get('media') 
           if media:
    
                update.media=media
                
           update.save()
                
           return redirect('admin')
    return render(request,'adminupdate.html',{'book':update})