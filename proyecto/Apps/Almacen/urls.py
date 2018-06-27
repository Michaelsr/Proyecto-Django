from django.conf.urls import url
from proyecto.Apps.Almacen.views import index
from proyecto.Apps.Almacen.views import almacen_view, almacen_list, almacen_edit, almacen_delete, \
	AlmacenList,AlmacenCreate,AlmacenUpdate, AlmacenDelete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', AlmacenCreate.as_view(), name='almacen_crear'),
    url(r'^listar$', AlmacenList.as_view(), name='almacen_listar'),
    url(r'^editar/(?P<pk>\d+)/$', AlmacenUpdate.as_view(), name='almacen_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',AlmacenDelete.as_view() , name='almacen_eliminar'),
]
