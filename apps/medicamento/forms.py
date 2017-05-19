from django import forms
from apps.medicamento.models import medicamento

class medicamento_form(forms.ModelForm):

    class Meta:
         model = medicamento
         fields = [
         'tipo',
         'nombre_comercial',
         'componente',
         'concentracion',
         'fecha_produccion',
         'fecha_expiracion',
         'descripcion',
         'stock',
         'costo_unidad',
         'venta_unidad',
         'proveedor',
         'presentacion',
         'lote',
         'estado',
          ]

         labels = {
             'tipo':'Tipo',
             'nombre_comercial':'Nombre Comercial',
             'componente':'Componentes',
             'concentracion':'Concentracion',
             'fecha_produccion':'Fecha Produccion',
             'fecha_expiracion':'Fecha Expiracion',
             'descripcion':'Descripcion(Indicaciones)',
             'stock':'Stock',
             'costo_unidad':'Costo Unidad',
             'venta_unidad':'Venta Unidad',
             'proveedor':'Proveedor',
             'presentacion':'Presentacion',
             'lote':'lote',
             'estado':'estado',

         }

         widgets = {
             'tipo':forms.Select(attrs={'class':'select','data-placeholder':'--Seleccione Tipo--',}),
             'nombre_comercial':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre Comercial'}),
             'componente':forms.TextInput(attrs={'class':'form-control','placeholder':'Componentes'}),
             'concentracion':forms.TextInput(attrs={'class':'form-control','placeholder':'ml/gr/ml/lt'}),
             'fecha_produccion':forms.TextInput(attrs={'class':'form-control','placeholder':'','id':'rangeDemoStart'}),
             'fecha_expiracion':forms.TextInput(attrs={'class':'form-control','placeholder':'','id':'rangeDemoFinish'}),
             'descripcion':forms.TextInput(attrs={'class':'form-control','placeholder':'Descripcion de Indicaciones'}),
             'stock':forms.TextInput(attrs={'class':'form-control','placeholder':'Numero de Productos','title':'Solo Nùmeros'}),
             'costo_unidad':forms.TextInput(attrs={'class':'form-control','placeholder':'Costo por unidad',}),
             'venta_unidad':forms.TextInput(attrs={'class':'form-control','placeholder':'Precio de venta'}),
             'proveedor':forms.Select(attrs={'class':'select','data-placeholder':'--Seleccione Proveedor--'}),
             'presentacion':forms.Select(attrs={'class':'select','data-placeholder':'--Seleccione Presentacion--',}),
             'lote': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'codigo de Lote'}),
             'estado': forms.CheckboxInput()
         }

class medicamento_form_actualizar(forms.ModelForm):

    class Meta:
         model = medicamento
         fields = [
         'id_medicamento',
         'tipo',
         'nombre_comercial',
         'componente',
         'concentracion',
         'fecha_produccion',
         'fecha_expiracion',
         'descripcion',
         'stock',
         'costo_unidad',
         'venta_unidad',
         'proveedor',
         'presentacion',
         'lote',
         'estado',
          ]

         labels = {
             'id_medicamento': 'id_medicamento',
             'tipo':'Tipo',
             'nombre_comercial':'Nombre Comercial',
             'componente':'Componentes',
             'concentracion':'Concentracion',
             'fecha_produccion':'Fecha Produccion',
             'fecha_expiracion':'Fecha Expiracion',
             'descripcion':'Descripcion(Indicaciones)',
             'stock':'Stock',
             'costo_unidad':'Costo Unidad',
             'venta_unidad':'Venta Unidad',
             'proveedor':'Proveedor',
             'presentacion':'Presentacion',
             'lote':'lote',
             'estado':'estado',

         }
         tipo_choices = (
             ('Comercial', 'Comercial'),
             ('Generico', 'Generico'),

         )
         widgets = {
             'id_medicamento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '','readonly':''}),
             'tipo':forms.Select(attrs={'class':'select','data-placeholder':'--Seleccione Tipo--',}),
             'nombre_comercial':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre Comercialxx'}),
             'componente':forms.TextInput(attrs={'class':'form-control','placeholder':'Componentes'}),
             'concentracion':forms.TextInput(attrs={'class':'form-control','placeholder':'ml/gr/ml/lt'}),
             'fecha_produccion':forms.TextInput(attrs={'class':'form-control','placeholder':'','id':'rangeDemoStart'}),
             'fecha_expiracion':forms.TextInput(attrs={'class':'form-control','placeholder':'','id':'rangeDemoFinish'}),
             'descripcion':forms.TextInput(attrs={'class':'form-control','placeholder':'Descripcion de Indicaciones'}),
             'stock':forms.TextInput(attrs={'class':'form-control','placeholder':'Numero de Productos','title':'Solo Nùmeros','pattern':'[0-9]'}),
             'costo_unidad':forms.TextInput(attrs={'class':'form-control','placeholder':'Costo por unidad',}),
             'venta_unidad':forms.TextInput(attrs={'class':'form-control','placeholder':'Precio de venta'}),
             'proveedor':forms.Select(attrs={'class':'select','data-placeholder':'--Seleccione Proveedor--'}),
             'presentacion':forms.Select(attrs={'class':'select','data-placeholder':'--Seleccione Presentacion--',}),
             'lote': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'codigo de Lote'}),
             'estado': forms.CheckboxInput()
         }