console.log('🐔 AyamJī loaded');

// ─────────────────────────────────────────
// FORMSET: Add / Remove Row Dinamis
// ─────────────────────────────────────────
document.addEventListener('DOMContentLoaded', function () {
    const container = document.getElementById('formset-container');
    const addBtn = document.getElementById('add-row');
    const totalFormsInput = document.querySelector('input[name="items-TOTAL_FORMS"]');
    const emptyTemplate = document.getElementById('empty-form-template');

    if (!container || !addBtn || !totalFormsInput) return;

    // ─── TAMBAH BARIS ───
    addBtn.addEventListener('click', function () {
        const currentCount = parseInt(totalFormsInput.value);

        // Ambil HTML dari template, ganti __prefix__ jadi index baru
        let newHtml = emptyTemplate.innerHTML.replace(/__prefix__/g, currentCount);

        // Masukkan ke container
        const temp = document.createElement('div');
        temp.innerHTML = newHtml.trim();
        const newRow = temp.firstElementChild;
        container.appendChild(newRow);

        // Update total forms
        totalFormsInput.value = currentCount + 1;

        // Render icon Lucide baru
        if (window.lucide) window.lucide.createIcons();

        // Pasang event listener untuk tombol remove di baris baru
        attachRemoveListener(newRow);
    });

    // ─── HAPUS BARIS ───
    function attachRemoveListener(row) {
        const removeBtn = row.querySelector('.remove-row');
        if (!removeBtn) return;

        removeBtn.addEventListener('click', function () {
            row.remove();
            // Catatan: kita TIDAK decrement TOTAL_FORMS.
            // Django tetap butuh konsistensi jumlah. Baris yang dihapus
            // akan diabaikan karena tidak punya data valid.
        });
    }

    // Pasang listener ke baris yang sudah ada (dari server render)
    document.querySelectorAll('.formset-row').forEach(attachRemoveListener);
});