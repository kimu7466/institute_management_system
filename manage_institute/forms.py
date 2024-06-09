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

class ResetPasswordForm(forms.Form):
    otp = forms.CharField(label='OTP', max_length=6)
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ResetPasswordForm, self).__init__(*args, **kwargs)

    def clean_otp(self):
        otp = self.cleaned_data['otp']
        if self.user.otp != otp:
            raise forms.ValidationError("Invalid OTP")
        return otp

    def save(self):
        new_password = self.cleaned_data['new_password']
        self.user.set_password(new_password)
        self.user.save()
