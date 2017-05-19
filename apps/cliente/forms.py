from django import forms
from apps.cliente.models import Cliente


class register_cliente_form(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=[
            'nombres',
            'apellidos',
            'dni',
            'sexo',
            'fnacimiento',
            'direccion',
            'telefono',
            'correo'
        ]
        labels={
            'nombres':'Nombres',
            'apellidos':'Apellidos',
            'dni':'DNI',
            'sexo':'Sexo',
            'fnacimiento':'F_Nacimiento',
            'direccion':'Direccion',
            'telefono':'Telefono',
            'correo':'Correo'

        }

        widgets={

            'nombres':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombres'}),
            'apellidos':forms.TextInput(attrs={'class':'form-control','placeholder':'Apellidos'}),
            'dni':forms.TextInput(attrs={'class':'form-control','placeholder':'Documento Nacional de Identidad','title':'Solo Nùmeros','pattern':'[0-9]{8}'}),
            'sexo':forms.Select(attrs={'class':'select','data-placeholder':'--Seleccione Genero--'}),
            'fnacimiento':forms.TextInput(attrs={'class':'form-control','placeholder':'Fecha Nacmiento','id':'anytime-month-numeric' }),
            'direccion':forms.TextInput(attrs={'class':'form-control','placeholder':'Direccion'}),
            'telefono':forms.TextInput(attrs={'class':'form-control','placeholder':'Telefono'}),
            'correo':forms.TextInput(attrs={'class':'form-control','placeholder':'Correo'})

        }


class update_cliente_form(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'id_cliente',
            'nombres',
            'apellidos',
            'dni',
            'sexo',
            'fnacimiento',
            'direccion',
            'telefono',
            'correo'
        ]
        labels = {
            'id_cliente': 'Id_Cliente',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'dni': 'DNI',
            'sexo': 'Sexo',
            'fnacimiento': 'F_Nacimiento',
            'direccion': 'Direccion',
            'telefono': 'Telefono',
            'correo': 'Correo'

        }

        widgets = {
            'id_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ID Cliente','type':'hidden'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombres'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
            'dni': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Documento Nacional de Identidad','title':'Solo Nùmeros','pattern':'[0-9]{8}'}),
            'sexo': forms.Select(attrs={'class': 'select', 'data-placeholder': '--Seleccione Genero--'}),
            'fnacimiento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fecha Nacmiento'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Direccion'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefono'}),
            'correo': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Correo','pattern':'[a-zA-Z0-9_]+([.][a-zA-Z0-9_]+)*@[a-zA-Z0-9_]+([.][a-zA-Z0-9_]+)*[.][a-zA-Z]{1,5}'})

        }




