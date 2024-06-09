from django.urls import path
from .views import *         

urlpatterns = [
    path('', welcome_view, name='welcome_view'),
    path('login_view/',login_view,name='login_view'),
    path('logout/',logout,name='logout'),
    path('student_login_view/', student_login_view, name='student_login_view'),
    path('register_teacher/', register_teacher, name='register_teacher'),
    path('home_view/', home_view, name='home_view'),
    path('student_home_view/', student_home_view, name='student_home_view'),

    
    path('clubs/', club_list, name='club_list'),
    path('clubs/create/', club_create, name='club_create'),
    path('clubs/<int:pk>/', club_detail, name='club_detail'),
    path('clubs/<int:pk>/update/', club_update, name='club_update'),
    path('clubs/<int:pk>/delete/', club_delete, name='club_delete'),


    path('books/', book_list, name='book_list'),
    path('books/create/', book_create, name='book_create'),
    path('books/<int:pk>/', book_detail, name='book_detail'),
    path('books/<int:pk>/update/', book_update, name='book_update'),
    path('books/<int:pk>/delete/', book_delete, name='book_delete'),


    path('students/', student_list, name='student_list'),
    path('students/create/', student_create, name='student_create'),
    path('students/<int:pk>/', student_detail, name='student_detail'),
    path('students/<int:pk>/update/', student_update, name='student_update'),
    path('students/<int:pk>/delete/', student_delete, name='student_delete'),
    
    path('rough_view/',rough_view, name='rough_view'),
    
    path('forgot_password/', forgot_password_view, name='forgot_password_view'),
    path('reset_password_otp_verification/', reset_password_otp_verification,
    name='reset_password_otp_verification'),
]    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

 
 
"""
    wrappers in Python when we want to modify or extend the behavior of an existing function, method, or class without modifying its source code

    decoreters:- chage the function behaviour with out changeing that actual code .    
    
    wrapper in python when we want to modify or extend the behavior of an exiting function,method, or class without modifying its source code .
    
    
    



"""