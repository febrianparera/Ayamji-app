"""
URL configuration for config project.

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
from django.shortcuts import render

from orders import views as orders_views


def login_view(request):
    return render(request, "pages/login.html")


def dashboard_view(request):
    context = {
        "menu": orders_views.get_menu(),
        "user_name": "Budi Direktur",
        "user_role": "Direktur",
    }
    return render(request, "pages/dashboard.html", context)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", login_view, name="login"),
    path("dashboard/", dashboard_view, name="dashboard"),

    # Modul Requests
        path("requests/", orders_views.requests_list_view, name="requests_list"),
    path("requests/new/", orders_views.requests_new_view, name="requests_new"), 

    # (sementara: view lain akan dipindah di sesi berikutnya)
]