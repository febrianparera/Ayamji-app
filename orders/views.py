from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from .models import ProductRequest, RequestItem
from .forms import ProductRequestForm, RequestItemForm
from .utils import generate_kode


def get_menu():
    return [
        {"label": "Dashboard",  "url": "/dashboard/",  "icon": "layout-dashboard"},
        {"label": "Permintaan", "url": "/requests/",   "icon": "clipboard-list"},
        {"label": "Nota",       "url": "/notas/",      "icon": "receipt"},
        {"label": "Inventory",  "url": "/inventory/",  "icon": "warehouse"},
        {"label": "Pengiriman", "url": "/delivery/",   "icon": "truck"},
    ]


def requests_list_view(request):
    """List semua permintaan dari database."""
    requests = ProductRequest.objects.all()

    context = {
        "menu": get_menu(),
        "user_name": "Admin",
        "user_role": "Admin",
        "requests": requests,
    }
    return render(request, "pages/requests/list.html", context)


def requests_new_view(request):
    """Form input order baru. Handle GET (tampilkan) & POST (simpan)."""
    if request.method == 'POST':
        # Data dikirim dari form
        form = ProductRequestForm(request.POST)

        if form.is_valid():
            # Simpan ke database, TAPI jangan commit dulu
            # (supaya kita bisa isi field yang tidak ada di form)
            req = form.save(commit=False)

            # Isi field otomatis
            req.kode = generate_kode()
            req.status = 'menunggu'

            # Sementara: ambil user pertama dari DB
            # (nanti setelah login asli, ganti jadi request.user)
            user = User.objects.first()
            req.input_by = user
            # Marketing dari form juga berupa User
            # Tapi form pakai dropdown "marketing" → sudah User

            req.save()

            # Redirect ke list dengan notifikasi sukses
            messages.success(request, f"Permintaan {req.kode} berhasil dibuat!")
            return redirect('requests_list')
        else:
            messages.error(request, "Ada kesalahan di form. Periksa kembali.")
    else:
        # GET — tampilkan form kosong
        form = ProductRequestForm()

    context = {
        "menu": get_menu(),
        "user_name": "Admin",
        "user_role": "Admin",
        "form": form,
    }
    return render(request, "pages/requests/form.html", context)