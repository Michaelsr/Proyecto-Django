from django.conf.urls import url
from proyecto.Apps.Venta.views import index

urlpatterns = [
    url(r'^$', index),
]
