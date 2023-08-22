from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

alpha_only_validator = RegexValidator(
    #para asegurarse que en el campo apellido y nombre no se ingresen numeros 
    regex=r'^[a-zA-Z]*$',
    message='Este campo debe contener solo letras.',
)



class Registro(forms.Form):
    '''Clase que contiene los campos del formulario de registro de clientes'''
    nombre = forms.CharField(required=True, min_length=3, max_length=10,validators=[alpha_only_validator] ,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Nombre Cliente'
    }))
    apellido =forms.CharField(required=True, min_length=3, max_length=20,validators=[alpha_only_validator],widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Apellido Cliente'
    }))
    username = forms.CharField(required=True, min_length=5,max_length=20, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Usuario'
    }))
    correo = forms.EmailField(required=True, min_length=6,max_length=40, widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'ejemplo@gmail.com'
    }))
    password = forms.CharField(required=True, min_length=6,max_length=20,widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Contraseña'
    }))



    def clean_username(self):
        '''Funcion para vaildar el usuario'''
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Usuario ya existente')#Si en la base de datos existe el usuario anteriormente
        
        return username
    

    
    def clean_email(self):
        correo=self.cleaned_data.get('correo')

        if User.objects.filter(correo=correo).exists():
            raise forms.ValidationError('Correo ya registrado')
        
        return correo
    

    
