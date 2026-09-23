from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import transaction

from .models import ProductRequest, RequestItem
from .forms import ProductRequestForm, RequestItemForm, RequestItemFormSet
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
    """Form input order + item dinamis. Handle GET & POST."""

    if request.method == 'POST':
        form = ProductRequestForm(request.POST)
        formset = RequestItemFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            try:
                with transaction.atomic():
                    # 1. Simpan ProductRequest (belum commit)
                    req = form.save(commit=False)
                    req.kode = generate_kode()
                    req.status = 'menunggu'
                    req.input_by = User.objects.first()
                    req.save()

                    # 2. Simpan semua RequestItem, terikat ke req
                    formset.instance = req
                    formset.save()

                messages.success(
                    request,
                    f"Permintaan {req.kode} berhasil dibuat dengan "
                    f"{req.items.count()} item!"
                )
                return redirect('requests_list')

            except Exception as e:
                messages.error(request, f"Gagal menyimpan: {e}")
        else:
            messages.error(request, "Ada kesalahan di form. Periksa kembali.")

    else:
        # GET — form kosong
        form = ProductRequestForm()
        formset = RequestItemFormSet()

    context = {
        "menu": get_menu(),
        "user_name": "Admin",
        "user_role": "Admin",
        "form": form,
        "formset": formset,
    }
    return render(request, "pages/requests/form.html", context)
    """Form input order + item dinamis. Handle GET & POST."""

    if request.method == 'POST':
        form = ProductRequestForm(request.POST)
        formset = RequestItemFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            try:
                with transaction.atomic():
                    # 1. Simpan ProductRequest (belum commit)
                    req = form.save(commit=False)
                    req.kode = generate_kode()
                    req.status = 'menunggu'
                    req.input_by = User.objects.first()
                    req.save()

                    # 2. Simpan semua RequestItem, terikat ke req
                    formset.instance = req
                    formset.save()

                messages.success(
                    request,
                    f"Permintaan {req.kode} berhasil dibuat dengan "
                    f"{req.items.count()} item!"
                )
                return redirect('requests_list')

            except Exception as e:
                messages.error(request, f"Gagal menyimpan: {e}")
        else:
            messages.error(request, "Ada kesalahan di form. Periksa kembali.")

    else:
        # GET — form kosong
        form = ProductRequestForm()
        formset = RequestItemFormSet()

    context = {
        "menu": get_menu(),
        "user_name": "Admin",
        "user_role": "Admin",
        "form": form,
        "formset": formset,
    }
    return render(request, "pages/requests/form.html", context)