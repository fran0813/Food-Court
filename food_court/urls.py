from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from main.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', index, name='index' ),
    url(r'^perfil$', perfil, name='perfil' ), 
    url(r'^mapa$', mapa, name='mapa' ),
    url(r'^contacto$', contacto, name='contacto' ), 
    url(r'^login$', login , name='login' ),
    url(r'^logout$', logout, name = 'logout' ),
    url(r'^registrar$', registrar_usuario, name='registrar-usuario' ),
    url(r'^registrar-cliente$', registrar_cliente, name='registrar-cliente' ),
    url(r'^principal$', principal , name='principal' ),

    url(r'^restaurante$', restaurante , name='restaurante' ),
    url(r'^restaurante/add$', add_restaurante , name='add-restaurante' ),
    url(r'^restaurante/(?P<pk>[0-9]+)/edit$', edit_restaurante, name='edit-restaurante'),
    url(r'^restaurante/(?P<pk>\d+)/remove/$', delete_restaurante, name='delete-restaurante'),
    url(r'^restaurante/(?P<pk>[0-9]+)/$', restaurante_detail, name='restaurante-detalle'),

    url(r'^menu/(?P<pk>[0-9]+)/$', menu_list , name='list-menu' ),
    url(r'^menu/(?P<pk>[0-9]+)/add$', add_menu , name='add-menu' ),
    url(r'^menu/(?P<pk>[0-9]+)/edit$', edit_menu, name='edit-menu'),
    url(r'^menu/(?P<pk>\d+)/remove/$', delete_menu, name='delete-menu'),

   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
