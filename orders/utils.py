from django.utils import timezone
from .models import ProductRequest


def generate_kode():
    """Generate kode unik: REQ-YYYY-NNN. Auto-increment per tahun."""
    tahun = timezone.now().year
    prefix = f"REQ-{tahun}-"

    last = (
        ProductRequest.objects
        .filter(kode__startswith=prefix)
        .order_by('-kode')
        .first()
    )

    if last:
        # Ambil angka terakhir, misal REQ-2024-005 → 5
        last_number = int(last.kode.split('-')[-1])
        new_number = last_number + 1
    else:
        new_number = 1

    # Format: 3 digit dengan leading zero → 001, 002, ..., 999
    return f"{prefix}{new_number:03d}"