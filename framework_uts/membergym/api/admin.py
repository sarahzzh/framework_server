from django.contrib import admin
from .models import Member, Trainer, Paket, Transaksi

# Member Admin Configuration
class MemberAdmin(admin.ModelAdmin):
    list_display = ('nama', 'alamat', 'email', 'nohp', 'tgl_join')
    list_per_page = 10
    search_fields = ('nama', 'email', 'alamat')
    ordering = ('nama',)

# Trainer Admin Configuration
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('nama', 'alamat', 'email', 'nohp', 'tgl_join')
    list_per_page = 10
    search_fields = ('nama', 'email', 'alamat')
    ordering = ('nama',)

# Paket Admin Configuration
class PaketAdmin(admin.ModelAdmin):
    list_display = ('nama', 'durasi', 'harga')
    list_per_page = 10
    search_fields = ('nama', 'durasi')
    ordering = ('nama',)

# Transaksi Admin Configuration
class TransaksiAdmin(admin.ModelAdmin):
    list_display = ('transaksi_id', 'member_id', 'trainer_id', 'tgl_transaksi', 'total')
    list_per_page = 10
    search_fields = ('transaksi_id', 'member_id', 'trainer_id')
    ordering = ('transaksi_id',)

# Register the models and their admin configurations
admin.site.register(Member, MemberAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Paket, PaketAdmin)
admin.site.register(Transaksi, TransaksiAdmin)
