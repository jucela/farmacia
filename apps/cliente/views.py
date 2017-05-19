from django.shortcuts import render,redirect
from apps.cliente.forms import register_cliente_form,update_cliente_form
from apps.cliente.models import Cliente

# Create your views here.
def register_cliente_view(request):
    if request.method == 'POST':
       form = register_cliente_form(request.POST)
       if form.is_valid():
          form.save()
       return redirect('register_cliente')
    else:
     form = register_cliente_form()
     return render(request,"cliente/registro_cliente.html",{'form':form})


def list_cliente_view(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, "cliente/gestion_cliente.html", context)

def update_cliente_view(request,id):
    id_cliente = Cliente.objects.get(id_cliente=id)
    if request.method == 'GET':
       form = update_cliente_form(instance=id_cliente)
    else:
        form = update_cliente_form(request.POST,instance=id_cliente)
        if form.is_valid():
          form.save()
          return redirect('list_cliente')

    return render(request,"cliente/editar_cliente.html",{'form':form})

