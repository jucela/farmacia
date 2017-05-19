from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

from apps.usuario.forms import usuario_form,usuario_form_registrar


def registrar_usuario(request):
    if request.method == 'POST':
        form = usuario_form_registrar(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            hola=messages.success(request, "Voto registrado. ¡Gracias por participar!")
            return redirect('usuario/registro_usuario.html',{'message':hola})
    else:
        form = usuario_form_registrar()
    return render(request, 'usuario/registro_usuario.html', {'form': form})

def usuario_list(request):
    if request.method == "POST":
            if "txtuser" in request.POST:
                    id = request.POST['txtuser']
                    p = User.objects.get(id=id)
                    p.delete()
                    return redirect('usuario_list')
            else:
                return redirect('usuario_list')
    else:
       usuarios=User.objects.all()
       context = {'usuarios':usuarios}
       return  render(request,"usuario/gestion_usuario.html",context)

def usuario_edit(request,id):
    id_user = User.objects.get(id=id)
    if request.method == 'GET':
        form = usuario_form(instance=id_user)
    else:
         form = usuario_form(request.POST,instance=id_user)
         if form.is_valid():
            form.save()
            return redirect('usuario_list')

    return render(request, "usuario/editar_usuario.html",{'form': form})




