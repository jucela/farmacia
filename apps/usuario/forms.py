from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class usuario_form(forms.ModelForm):
    # estado_choices = (
    #     ('1', 'Activo'),
    #     ('0', 'Inactivo'),
    #
    # )
    id = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "id",'readonly':''}))
    username = forms.CharField(max_length=30,help_text='Optional.', widget=forms.TextInput(attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': "Ingrese Usuario",'readonly':''}))
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.',widget=forms.TextInput(attrs={'maxlength':30,'class':'form-control','placeholder':"Ingrese Nombres"}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.',widget=forms.TextInput(attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': "Ingrese Apellidos"}))
    email = forms.EmailField(max_length=254,help_text='Required. Inform a valid email address.',widget=forms.TextInput(attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': "Ingrese correo electronico"}))
    is_staff = forms.BooleanField(required=False,widget=forms.CheckboxInput())
    is_active = forms.BooleanField(required=False,widget=forms.CheckboxInput())
    # is_staff = forms.BooleanField( widget=forms.RadioSelect(choices=estado_choices,attrs={}))
    class Meta:
        model = User
        fields = ('id','username', 'first_name', 'last_name', 'email','is_staff','is_active')

class usuario_form_registrar(UserCreationForm):
    # estado_choices = (
    #     ('1', 'Activo'),
    #     ('0', 'Inactivo'),
    #
    # )
    username = forms.CharField(max_length=30,help_text='Optional.', widget=forms.TextInput(attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': "Ingrese Usuario"}))
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.',widget=forms.TextInput(attrs={'maxlength':30,'class':'form-control','placeholder':"Ingrese Nombres"}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.',widget=forms.TextInput(attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': "Ingrese Apellidos"}))
    password1 = forms.CharField(max_length=30,help_text='Optional.', widget=forms.PasswordInput(attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': "Ingrese Contraseña"}))
    password2 = forms.CharField(max_length=30,help_text='Optional.',widget=forms.PasswordInput(attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': "Vuelva a ingresar contraseña"}))
    email = forms.EmailField(max_length=254,help_text='Required. Inform a valid email address.',widget=forms.TextInput(attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': "Ingrese correo electronico"}))
    is_staff = forms.BooleanField(required=False,widget=forms.CheckboxInput())
    is_active = forms.BooleanField(required=False,widget=forms.CheckboxInput())
    # is_staff = forms.ChoiceField(choices=estado_choices,widget=forms.RadioSelect())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','is_staff','is_active' )

