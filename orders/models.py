from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    """Pelanggan toko ayam."""
    nama = models.CharField(max_length=100)
    telepon = models.CharField(max_length=20, blank=True)
    alamat = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama

    class Meta:
        ordering = ['nama']
        verbose_name_plural = "Customers"


class Product(models.Model):
    """Produk yang dijual: ayam beku, nugget, dsb."""
    UNIT_CHOICES = [
        ('kg', 'Kilogram'),
        ('pack', 'Pack'),
        ('box', 'Box'),
    ]

    nama = models.CharField(max_length=100)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default='kg')
    harga = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    is_nugget = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nama} ({self.unit})"

    class Meta:
        ordering = ['nama']


class ProductRequest(models.Model):
    """Permintaan order dari marketing (via WA)."""
    STATUS_CHOICES = [
        ('menunggu', 'Menunggu Timbang'),
        ('ditimbang', 'Sudah Ditimbang'),
        ('nota', 'Nota Dibuat'),
        ('batal', 'Batal'),
    ]
    SOURCE_CHOICES = [
        ('whatsapp', 'WhatsApp'),
        ('telepon', 'Telepon'),
        ('walk_in', 'Datang Langsung'),
    ]

    kode = models.CharField(max_length=30, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='requests')
    marketing = models.ForeignKey(User, on_delete=models.PROTECT, related_name='requests_as_marketing')
    input_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='requests_as_admin')
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES, default='whatsapp')
    wa_message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='menunggu')
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.kode

    class Meta:
        ordering = ['-created_at']


class RequestItem(models.Model):
    """Satu baris produk dalam permintaan."""
    request = models.ForeignKey(ProductRequest, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    qty_requested = models.DecimalField(max_digits=10, decimal_places=2)
    qty_weighed = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    note = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.product.nama} x {self.qty_requested}"

    @property
    def selisih(self):
        """Hitung selisih qty_weighed - qty_requested."""
        if self.qty_weighed is None:
            return None
        return self.qty_weighed - self.qty_requested
