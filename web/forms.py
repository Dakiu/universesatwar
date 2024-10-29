from django import forms

class UserForm(forms.Form):
    nombre = forms.CharField(max_length=50) 
    correo = forms.EmailField(max_length=100) 
    contrasena =forms.CharField(max_length=20)