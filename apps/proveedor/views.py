from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView
from apps.proveedor.models import proveedor
from apps.proveedor.forms  import register_proveedor_form,edit_proveedor_form

# Create your views here.
class register_proveedor_view(CreateView):
    model = proveedor
    form_class = register_proveedor_form
    template_name = 'proveedor/registro_proveedor.html'
    success_url = reverse_lazy('register_proveedor')

class edit_proveedor_view(UpdateView):
    model = proveedor
    form_class = edit_proveedor_form
    template_name = 'proveedor/editar_proveedor.html'
    success_url = reverse_lazy('list_proveedor')

class list_proveedor_view(ListView):
    model=proveedor
    template_name = 'proveedor/gestion_proveedor.html'
