from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from main.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', index, name='index' ), #/
    url(r'^login$', login , name='login' ),
    url(r'^logout$', logout, name = 'logout' ),
    url(r'^registrar$', registrar_usuario, name='registrar-usuario' ),
    url(r'^registrar-cliente$', registrar_cliente, name='registrar-cliente' ),
    url(r'^principal$', principal , name='principal' ),
    url(r'^restaurante$', restaurante , name='restaurante' ),
    url(r'^restaurante/add$', add_restaurante , name='add-restaurante' ),
    url(r'^restaurante/(?P<pk>[0-9]+)/$', restaurante_detail, name='restaurante-detalle')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
