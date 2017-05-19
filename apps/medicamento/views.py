from django.shortcuts import render,redirect
from apps.medicamento.forms import medicamento_form,medicamento_form_actualizar
from apps.medicamento.models import medicamento
from django.contrib import messages

# Create your views here.
def registro_medicamentoaa(request):
    return render(request,"medicamento/registro_medicamento.html")

def registro_medicamento(request):
    if request.method == 'POST':
       form = medicamento_form(request.POST)
       if form.is_valid():
          form.save()
          # hola = messages.success(request, "Voto registrado. ¡Gracias por participar!",{'form':form})
       return redirect('create_medicamento')
    else:
        form = medicamento_form()
        return render(request,"medicamento/registro_medicamento.html",{'form':form})

def gestionar_medicamento(request):
       medicamentos=medicamento.objects.all()
       context = {'medicamentos':medicamentos}
       return  render(request,"medicamento/gestion_medicamento.html",context)

def actualizar_medicamento(request,id):
    id_medicamento = medicamento.objects.get(id_medicamento=id)
    if request.method == 'GET':
        form = medicamento_form_actualizar(instance=id_medicamento)
    else:
         form = medicamento_form_actualizar(request.POST,instance=id_medicamento)
         if form.is_valid():
            form.save()
            return redirect('list_medicamento')

    return render(request, "medicamento/editar_medicamento.html",{'form': form})


def buscar_medicamento(request):
    medicamentos = medicamento.objects.all()
    context = {'medicamentos': medicamentos}
    return render(request, "medicamento/buscar_medicamento.html", context)
