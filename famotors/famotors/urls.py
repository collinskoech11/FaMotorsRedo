"""famotors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from fasite import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('Contact.html', views.Contact, name='Contact'),
    path('Gallery.html', views.Gallery, name='Gallery'),
    path('Recovery.html', views.Recovery, name='Recovery'),
    path('Service.html', views.Service, name='Service'),
    path('Team.html', views.Team, name='Team'),
    path('register.html', views.register, name='register'),
    path('Quotation.html', views.Quotation, name='Quotation'),
    path('Warranty.html', views.Warranty, name='Warranty'),
    path('Excess.html', views.Excess, name='Excess'),
    path('login.html',auth_view.LoginView.as_view(template_name='login.html')),
    path('logout.html', auth_view.LogoutView.as_view(template_name='logout.html')),
]

