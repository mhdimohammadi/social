from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import *


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=250, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=250, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=250, widget=forms.PasswordInput, required=True, label='password')
    password2 = forms.CharField(max_length=250, widget=forms.PasswordInput, required=True, label='repeat password')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'phone']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("رمز ها مطابقت ندارند!")
        return cd['password2']

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if User.objects.filter(phone=phone).exists():
            raise forms.ValidationError("phone already exist!")
        return phone


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'bio', 'date_of_birth', 'job', 'photo', 'username']

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if User.objects.exclude(id=self.instance.id).filter(phone=phone).exists():
            raise forms.ValidationError("phone already exist!")
        return phone

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(id=self.instance.id).filter(username=username).exists():
            raise forms.ValidationError("username already eexist!")
        return username


class TicketForm(forms.Form):
    SUBJECT_CHOICES = (
        ('پیشنهاد', 'پیشنهاد'),
        ('انتقاد', 'انتقاد'),
        ('گزارش', 'گزارش')
    )
    message = forms.CharField(widget=forms.Textarea, required=True, label="Message")
    name = forms.CharField(required=True, max_length=250, label="Name")
    email = forms.EmailField(label="Email")
    phone = forms.CharField(max_length=11, required=True, label="Phone")
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES, label="Subject")

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone:
            if not phone.isnumeric():
                raise forms.ValidationError('شماره تلفن عددی نیست')
            else:
                return phone


class CreatePostForm(forms.ModelForm):
    image1 = forms.ImageField(required=False)
    image2 = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['description', 'tags']


