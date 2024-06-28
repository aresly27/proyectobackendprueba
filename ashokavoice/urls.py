"""
URL configuration for ashokavoice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from usuario.views import CreateUsuario
from logro.views import LogroView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('put/<int:usuario_id>', CreateUsuario.as_view(), name='UpdateUsuario'),
    path('put/', CreateUsuario.as_view(), name='CreateUsuario'),
    path('delete/<int:usuario_id>', CreateUsuario.as_view(), name='DeleteUsuario'),
    
    path('put/logro', LogroView.as_view(), name='Crear logro'),
    path('put/logro/<int:logro_id>', LogroView.as_view(), name='UpdateLogro'),
    
    path('delete/<int:logro_id>', LogroView.as_view(), name='DeleteLogro'),

]
