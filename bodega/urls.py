"""bodega URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from apps.inicio.views import inicio
from apps.usuario.views import registrar_usuario,usuario_list,usuario_edit
from apps.empleado.views import registro_empleado
# from apps.privilegio.views import asignar_privilegio
from django.contrib.auth.views import login,logout_then_login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from apps.medicamento.views import registro_medicamento,gestionar_medicamento,actualizar_medicamento,buscar_medicamento
from apps.comprobante.views import boleta_view,agregar_medicamento
from apps.cliente.views import register_cliente_view,list_cliente_view,update_cliente_view
from apps.proveedor.views import register_proveedor_view,edit_proveedor_view,list_proveedor_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^inicio',inicio,name='inicio'),
    url(r'^registrarusuario/',registrar_usuario,name='registrar_usuario'),
    # url(r'^usuario/',usuario_view,name='usuario_view'),
    url(r'^gestionusuario/',usuario_list, name='usuario_list'),
    url(r'^editarusuario/(?P<id>[^/]+)/$',usuario_edit,name='usuario_edit'),
    url(r'^empleado',registro_empleado),
    # url(r'^privilegio',asignar_privilegio),
    url(r'^accounts/login/',login,{'template_name':'index.html'}, name='login'),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^reset/password_reset', password_reset,
        {'template_name':'usuario/password_reset_form.html',
        'email_template_name': 'usuario/password_reset_email.html'},
        name='password_reset'),
    url(r'^password_reset_done',password_reset_done,
        {'template_name': 'usuario/password_reset_done.html'},
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',password_reset_confirm,
        {'template_name': 'usuario/password_reset_confirm.html'},
        name='password_reset_confirm'
        ),
    url(r'^reset/done', password_reset_complete,{'template_name': 'usuario/password_reset_complete.html'},
        name='password_reset_complete'),
#
    url(r'^recuperarusuario', password_reset,
        {'template_name': 'usuario/password_reset_form_pag.html',
         'email_template_name': 'usuario/password_reset_email.html'},
        name='recuperarusuario'),
    url(r'^registrarmedicamento',registro_medicamento,name='create_medicamento'),
    url(r'^gestionarmedicamento',gestionar_medicamento,name='list_medicamento'),
    url(r'^editarmedicamento/(?P<id>[^/]+)/$',actualizar_medicamento,name='edit_medicamento'),
    url(r'^buscarmedicamento',buscar_medicamento,name='search_medicamento'),
    url(r'^mostrarboleta',boleta_view,name='view_boleta'),
    url(r'^registercliente',register_cliente_view,name='register_cliente'),
    url(r'^editcliente/(?P<id>[^/]+)/$',update_cliente_view,name='edit_cliente'),
    url(r'^gestioncliente',list_cliente_view,name='list_cliente'),
    url(r'^registerproveedor',register_proveedor_view.as_view(), name='register_proveedor'),
    url(r'^editproveedor/(?P<pk>[^/]+)/$',edit_proveedor_view.as_view(), name='edit_proveedor'),
    url(r'^gestionproveedor',list_proveedor_view.as_view(), name='list_proveedor'),

]
