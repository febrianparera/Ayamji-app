from django import forms
from .models import ProductRequest, RequestItem


class ProductRequestForm(forms.ModelForm):
    """Form untuk membuat ProductRequest baru."""

    class Meta:
        model = ProductRequest
        fields = ['customer', 'marketing', 'source', 'wa_message', 'note']
        widgets = {
            'customer': forms.Select(attrs={
                'class': 'w-full mt-1 px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-slate-900',
            }),
            'marketing': forms.Select(attrs={
                'class': 'w-full mt-1 px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-slate-900',
            }),
            'source': forms.Select(attrs={
                'class': 'w-full mt-1 px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-slate-900',
            }),
            'wa_message': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Contoh: "Bang, order 20 kg paha atas untuk Pak Andi"',
                'class': 'w-full mt-1 px-3 py-2 border rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-slate-900',
            }),
            'note': forms.Textarea(attrs={
                'rows': 2,
                'placeholder': 'Contoh: tolong dipisah per 5kg',
                'class': 'w-full mt-1 px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-slate-900',
            }),
        }
        labels = {
            'customer': 'Customer',
            'marketing': 'Marketing',
            'source': 'Sumber Order',
            'wa_message': 'Referensi Pesan WA (opsional)',
            'note': 'Catatan (opsional)',
        }


class RequestItemForm(forms.ModelForm):
    """Form untuk satu baris item."""

    class Meta:
        model = RequestItem
        fields = ['product', 'qty_requested', 'note']
        widgets = {
            'product': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-slate-900',
            }),
            'qty_requested': forms.NumberInput(attrs={
                'placeholder': 'Qty',
                'class': 'w-full px-3 py-2 border rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-slate-900',
                'step': '0.01',
                'min': '0',
            }),
            'note': forms.TextInput(attrs={
                'placeholder': 'Catatan',
                'class': 'w-full px-3 py-2 border rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-slate-900',
            }),
        }

from django.forms import inlineformset_factory

RequestItemFormSet = inlineformset_factory(
parent_model=ProductRequest,
model=RequestItem,
form=RequestItemForm,
fields=['product', 'qty_requested', 'note'],
extra=1,           
can_delete=True,   
)