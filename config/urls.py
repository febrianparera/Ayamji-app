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


# ─────────────────────────────────────────
# MOCK DATA (sementara)
# Nanti diganti dengan data dari database.
# ─────────────────────────────────────────
def get_mock_requests():
    return [
        {
            "id": "REQ-001",
            "kode": "REQ-2024-001",
            "customer": "Toko Berkah",
            "marketing": "Andi",
            "items_count": 3,
            "status": "menunggu",
            "status_label": "Menunggu Timbang",
            "status_color": "warning",
            "created_at": "2024-06-01 09:12",
        },
        {
            "id": "REQ-002",
            "kode": "REQ-2024-002",
            "customer": "RM Sederhana",
            "marketing": "Rina",
            "items_count": 5,
            "status": "ditimbang",
            "status_label": "Sudah Ditimbang",
            "status_color": "info",
            "created_at": "2024-06-01 10:30",
        },
        {
            "id": "REQ-003",
            "kode": "REQ-2024-003",
            "customer": "Warung Bu Yati",
            "marketing": "Andi",
            "items_count": 2,
            "status": "nota",
            "status_label": "Nota Dibuat",
            "status_color": "success",
            "created_at": "2024-05-31 14:55",
        },
    ]


def get_mock_request_detail():
    return {
        "kode": "REQ-2024-001",
        "customer": "Toko Berkah",
        "marketing": "Andi",
        "admin": "Wati",
        "source": "whatsapp",
        "status": "menunggu",
        "status_label": "Menunggu Timbang",
        "status_color": "warning",
        "created_at": "01 Juni 2024, 09:12",
        "wa_message": "Bang, order 20 kg paha atas dan 10 kg sayap untuk Pak Andi ya",
        "items": [
            {"name": "Paha Atas",  "qty_requested": 20, "qty_weighed": None, "unit": "kg", "selisih": None},
            {"name": "Sayap",      "qty_requested": 10, "qty_weighed": None, "unit": "kg", "selisih": None},
            {"name": "Nugget 500gr","qty_requested": 3, "qty_weighed": None, "unit": "pack", "selisih": None},
        ],
    }


# ─────────────────────────────────────────
# MENU per role (nanti diganti sesuai user)
# ─────────────────────────────────────────
def get_menu():
    return [
        {"label": "Dashboard",  "url": "/dashboard/",  "icon": "layout-dashboard"},
        {"label": "Permintaan", "url": "/requests/",   "icon": "clipboard-list"},
        {"label": "Nota",       "url": "/notas/",      "icon": "receipt"},
        {"label": "Inventory",  "url": "/inventory/",  "icon": "warehouse"},
        {"label": "Pengiriman", "url": "/delivery/",   "icon": "truck"},
    ]


# ─────────────────────────────────────────
# VIEWS
# ─────────────────────────────────────────
def login_view(request):
    return render(request, "pages/login.html")


def dashboard_view(request):
    context = {
        "menu": get_menu(),
        "user_name": "Budi Direktur",
        "user_role": "Direktur",
    }
    return render(request, "pages/dashboard.html", context)


def requests_list_view(request):
    context = {
        "menu": get_menu(),
        "user_name": "Wati Admin",
        "user_role": "Admin",
        "requests": get_mock_requests(),
    }
    return render(request, "pages/requests/list.html", context)


def requests_new_view(request):
    context = {
        "menu": get_menu(),
        "user_name": "Wati Admin",
        "user_role": "Admin",
    }
    return render(request, "pages/requests/form.html", context)


def requests_detail_view(request, request_id):
    context = {
        "menu": get_menu(),
        "user_name": "Wati Admin",
        "user_role": "Admin",
        "request_data": get_mock_request_detail(),
    }
    return render(request, "pages/requests/detail.html", context)


# ─────────────────────────────────────────
# URL ROUTING
# ─────────────────────────────────────────
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", login_view, name="login"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("requests/", requests_list_view, name="requests_list"),
    path("requests/new/", requests_new_view, name="requests_new"),
    path("requests/<str:request_id>/", requests_detail_view, name="requests_detail"),
]