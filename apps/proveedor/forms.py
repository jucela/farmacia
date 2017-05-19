from django import forms
from apps.proveedor.models import proveedor

class register_proveedor_form(forms.ModelForm):
    class Meta:
        model=proveedor
        fields=[
            'ruc',
            'nombre',
            'razon_social',
            'direccion',
            'telefono',
            'correo'
        ]
        labels={
            'ruc':'RUC',
            'nombre':'Nombre',
            'razon_social':'Razon Social',
            'direccion':'Direccion',
            'telefono':'Telefono',
            'correo':'Correo'

        }

        widgets={

            'ruc':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Registro Unico de Contribuyente','title':'Solo Nùmeros','pattern':'[0-9]{11}'}),
            'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre Comercial'}),
            'razon_social':forms.TextInput(attrs={'class':'form-control','placeholder':'Razon Social'}),
            'direccion':forms.TextInput(attrs={'class':'form-control','placeholder':'Direccion'}),
            'telefono':forms.TextInput(attrs={'class':'form-control','placeholder':'Telefono'}),
            'correo':forms.TextInput(attrs={'class':'form-control','placeholder':'Correo'})

        }
class edit_proveedor_form(forms.ModelForm):
    class Meta:
        model=proveedor
        fields=[
            'id_proveedor',
            'ruc',
            'nombre',
            'razon_social',
            'direccion',
            'telefono',
            'correo'
        ]
        labels={
            'id_proveedor':'',
            'ruc':'RUC',
            'nombre':'Nombre',
            'razon_social':'Razon Social',
            'direccion':'Direccion',
            'telefono':'Telefono',
            'correo':'Correo'

        }

        widgets={
            'id_proveedor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '','readonly':''}),
            'ruc':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Registro Unico de Contribuyente','title':'Solo Nùmeros','pattern':'[0-9]{11}'}),
            'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre Comercial'}),
            'razon_social':forms.TextInput(attrs={'class':'form-control','placeholder':'Razon Social'}),
            'direccion':forms.TextInput(attrs={'class':'form-control','placeholder':'Direccion'}),
            'telefono':forms.TextInput(attrs={'class':'form-control','placeholder':'Telefono'}),
            'correo':forms.TextInput(attrs={'class':'form-control','placeholder':'Correo'})

        }