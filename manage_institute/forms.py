from django import forms
from .models import Club , Book, Student

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name', 'description']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['email', 'password', 'name', 'roll_number', 'age', 'department']


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=254)
