from django.shortcuts import render
from apps.medicamento.models import medicamento

# Create your views here.
def boleta_view(request):
    medicamentos = medicamento.objects.all()
    context = {'medicamentos': medicamentos}
    return render(request,"comprobante/boleta.html",context)

def agregar_medicamento(request):
    medicamentos = medicamento.objects.all()
    context = {'medicamentos': medicamentos}
    return render(request, "comprobante/boleta.html", context)

