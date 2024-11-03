from django import forms

class UserForm(forms.Form):
    nombre = forms.CharField(max_length=50) 
    contrasena =forms.CharField(max_length=20, widget=forms.PasswordInput, label="Contraseña")