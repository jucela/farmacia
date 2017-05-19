from django.shortcuts import render,redirect
# from apps.usuario.forms import usuario_form
# from apps.usuario.forms import usuario_form
# from apps.usuario.models import usuario
#
# # Create your views here.
def registro_empleado(request):
    return render(request,"empleado/registro_empleado.html")
# # Muestra formulario gestion_usuario.html.
# def gestion_usuario(request):
#    return render(request,"usuario/gestion_usuario.html")
# # Muestra formulario registrar_usuario.html.
# def registro_usuario(request):
#     return render(request,"usuario/registro_usuario.html")
# # Muestra formulario editar_usuario.html.
# def editar_usuario(request):
#
#     form = usuario_form()
#     return render(request,"usuario/editar_usuario.html",{'form':form})
#
#
# #Registra Usuario en la base de  datos , tabla (usuario_usuario)
# def usuario_view(request):
#     if request.method == 'POST':
#         form = usuario_form(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('usuario_view')
#     else:
#             form = usuario_form()
#     return render(request,"usuario/registro_usuario.html",{'form':form})
#
# def usuario_list(request):
#     if request.method == "POST":
#         if "txtuser" in request.POST:
#                 user = request.POST['txtuser']
#                 p = usuario.objects.get(usuario=user)
#                 p.delete()
#                 return redirect('usuario_list')
#         else:
#             return redirect('usuario_list')
#     else:
#        usuarios=usuario.objects.all()
#        context = {'usuarios':usuarios}
#        return  render(request,"usuario/gestion_usuario.html",context)
#
# def usuario_edit(request,user):
#     id_user = usuario.objects.get(usuario=user)
#     if request.method == 'GET':
#         form = usuario_form(instance=id_user)
#     else:
#         form = usuario_form(request.POST,instance=id_user)
#         if form.is_valid():
#              form.save()
#         return redirect('usuario_list')
#     return render(request, "usuario/editar_usuario.html",{'form': form})

# # def usuario_delete(request,user):
# #     id_user = usuario.objects.get(usuario=user)
# #     if request.method == 'POST':
# #         id_user.delete()
# #         return redirect('usuario_list')
# #      return