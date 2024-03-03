"""
URL configuration for sem1 project.

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
import pdb

from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.forms import AuthenticationForm, forms

secured_af = {"login": "ILook", "pw": "IntoYourEyes"}

AdminSite.site_header = gettext_lazy(f'''login:'{secured_af["login"]}' pw:"{secured_af["pw"]}"''')
AuthenticationForm.declared_fields['username'].initial = secured_af["login"]
AuthenticationForm.declared_fields['password'].widget = forms.PasswordInput(
    attrs={"autocomplete": "current-password", "value": secured_af["pw"]})

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("app1.urls")),
    path('rands/', include('app2_randoms.urls'))
]
