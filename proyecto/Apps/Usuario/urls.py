from django.conf.urls import url
from proyecto.Apps.Usuario.views import RegistroUsuario

urlpatterns = [
	url(r'^registrar', RegistroUsuario.as_view(), name="registrar")

]
