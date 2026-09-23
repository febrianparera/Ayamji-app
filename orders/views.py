from django.shortcuts import render
from .models import ProductRequest


def requests_list_view(request):
    """Tampilkan semua permintaan dari database."""
    requests = ProductRequest.objects.all()

    context = {
        "menu": get_menu(),
        "user_name": "Admin",
        "user_role": "Admin",
        "requests": requests,
    }
    return render(request, "pages/requests/list.html", context)


def get_menu():
    return [
        {"label": "Dashboard",  "url": "/dashboard/",  "icon": "layout-dashboard"},
        {"label": "Permintaan", "url": "/requests/",   "icon": "clipboard-list"},
        {"label": "Nota",       "url": "/notas/",      "icon": "receipt"},
        {"label": "Inventory",  "url": "/inventory/",  "icon": "warehouse"},
        {"label": "Pengiriman", "url": "/delivery/",   "icon": "truck"},
    ]