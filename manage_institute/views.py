from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings
from django.http import HttpResponse
from .models import Teacher
from .forms import ForgotPasswordForm, ResetPasswordForm
from .utils.otp import generate_otp
from .models import Teacher, Department, Student, Club, Book
from .forms import ClubForm, BookForm,  StudentForm

def is_logged_in(func):
     def wrapper(request, *args, **kwargs):
          if "email" in request.session:
               return func(request, *args, **kwargs)
          return redirect('welcome_view')
     return wrapper

def welcome_view(request):
     return render(request, "welcome.html")

def register_teacher(request):
     if request.method == 'POST':
          email = request.POST['email']
          password = request.POST['password']
          name = request.POST['name']
          department_id = request.POST['department']
          department = Department.objects.get(id=department_id)
          
          Teacher.objects.create(email=email, password=password, name=name, department=department)
          return redirect('login_view')  
     
     departments = Department.objects.all()
     return render(request, 'register_teacher.html', {'departments': departments})

def login_view(request):
     if request.method == 'POST':
          email = request.POST.get('email')
          password = request.POST.get('password')
          try:
               get_teacher = Teacher.objects.get(email = email)
          except Exception as e:
               print("error", e)
          else:
               if get_teacher.email == email:
                    if get_teacher.password == password:
                         request.session['email'] = email
                         request.session['name'] = get_teacher.name
                         request.session['department_id'] = get_teacher.department.id
                         request.session['department_name'] = get_teacher.department.name
                         return redirect('home_view')
     return render(request, 'login.html')
 
def rough_view(request):
    return render(request, 'rough.html')


@is_logged_in
def home_view(request):
    students = Student.objects.all().count()
    teachers = Teacher.objects.all().count()
    clubs = Club.objects.all().count()                     
    books = Book.objects.all().count()                     

    context = {"students_count":students,
               "teachers_count":teachers,
               "clubs_count":clubs, 
               "books_count":books }
    return render(request, "home.html", context)

def student_login_view(request):
     if request.method == 'POST':
          email = request.POST.get('email')
          password = request.POST.get('password')
          try:
               get_student = Student.objects.get(email = email)
          except Exception as e:
               print("error", e)
          else:
               if get_student.email == email:
                    if get_student.password == password:
                         request.session['email'] = email
                         request.session['name'] = get_student.name
                         request.session['roll_number'] = get_student.roll_number
                         request.session['age'] = get_student.age
                         request.session['department_id'] = get_student.department.id
                         request.session['department_name'] = get_student.department.name
                         return redirect('student_home_view')
     return render(request, "student_login.html")

@is_logged_in
def student_home_view(request):
     return render(request, "for_students/s_home.html")

@is_logged_in
def logout(request):
     request.session.clear()
     return redirect('welcome_view')



@is_logged_in
def club_create(request):
    # print(clubs)
    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('club_list')
    else:
        form = ClubForm()
    return render(request, 'for_club/club_form.html', {'form': form})

@is_logged_in
def club_list(request):
    clubs = Club.objects.all()
    return render(request, 'for_club/club_list.html', {'clubs': clubs})

@is_logged_in
def club_detail(request, pk):
    club = get_object_or_404(Club, pk=pk)
    return render(request, 'for_club/club_detail.html', {'club': club})

@is_logged_in
def club_update(request, pk):
    club = get_object_or_404(Club, pk=pk)
    if request.method == 'POST':
        form = ClubForm(request.POST, instance=club)
        if form.is_valid():
            form.save()
            return redirect('club_detail', pk=club.pk)
    else:
        form = ClubForm(instance=club)
    return render(request, 'for_club/club_form.html', {'form': form})

@is_logged_in
def club_delete(request, pk):
    club = get_object_or_404(Club, pk=pk)
    if request.method == 'POST':
        club.delete()
        return redirect('club_list')
    return render(request, 'for_club/club_confirm_delete.html', {'club': club})



@is_logged_in
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'for_book/book_form.html', {'form': form})

@is_logged_in
def book_list(request):
    books = Book.objects.all()
    return render(request, 'for_book/book_list.html', {'books': books})

@is_logged_in
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'for_book/book_detail.html', {'book': book})

@is_logged_in
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'for_book/book_form.html', {'form': form})

@is_logged_in
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'for_book/book_confirm_delete.html', {'book': book})


@is_logged_in
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'for_student/student_form.html', {'form': form})

@is_logged_in
def student_list(request):
    students = Student.objects.all()
    return render(request, 'for_student/student_list.html', {'students': students})

@is_logged_in
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'for_student/student_detail.html', {'student': student})

@is_logged_in
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'for_student/student_form.html', {'form': form}) 

@is_logged_in
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'for_student/student_confirm_delete.html', {'student': student})



def forgot_password_view(request):
    if request.method == 'POST':
        email_ = request.POST['email']
        action = request.POST.get('action') 
        try:
            check_user = Student.objects.get(email=email_)
            print("this is user",check_user)
        except Student.DoesNotExist:
            print("THIS User doesn't exist")
        else:
            print("else")
            if check_user:
                if action == 'resend_otp':
                    otp_ = generate_otp(6)
                    subject = "Authentication Code for [Forgot password]"
                    message = f"Code for [Password Change]: {otp_}"
                    from_email = settings.EMAIL_HOST_USER
                    recipient_list = [f"{email_}"]
                    send_mail(subject, message, from_email, recipient_list)
                    check_user.otp = otp_
                    check_user.save()
                    return JsonResponse({'success': True, 'message': 'OTP Resent successfully'})

                otp_ = generate_otp(6)
                subject = "Authentication Code for [Forgot password]"
                message = f"Code for [Password Change]: {otp_}"
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [f"{email_}"]
                send_mail(subject, message, from_email, recipient_list)
                check_user.otp = otp_
                check_user.save()
                context = {'cum_email': email_}
                return render(request, 'change_password.html', context)
    return render(request, 'forgot.html')


def reset_password_otp_verification(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        entered_otp = request.POST.get('otp')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        
        if new_password != confirm_password:
            return HttpResponse("Passwords do not match")

        student = get_object_or_404(Student, email=email)

        
        if student.otp == entered_otp:
           
            student.password =new_password
            student.save()
            return HttpResponse("Password successfully reset")
        else:
            return HttpResponse("Invalid OTP")

    return render(request, 'reset_password_otp_verification.html')






