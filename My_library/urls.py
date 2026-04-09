"""
URL configuration for My_library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.usersignup,name='signup'),
    path('login/',views.userlogin,name='login'),
    path('home/',views.home,name='home'),
    path('book/',views.books,name='book'),
    path('book_issue/',views.books_issue,name='issue'),
    path('book_form/<int:id>/',views.book_form,name='form'),
    path('media_form/',views.first_models_form,name='form2'),
    path('book_form1/',views.book_form1,name='form3'),
    path('adminabid/',views.adminabid,name='admin'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('adminsearch/',views.admin_search,name='adminsrch'),
    path('admindelete/<int:id>/',views.admin_delete,name='delete'),
    path('adminupdate/<int:id>/',views.admin_update,name='update'),
    ]
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
