from django.contrib import admin
from .models import Profanity


# Register your models here for admin panel
@admin.register(Profanity)
class ProfanityAdmin(admin.ModelAdmin):
    list_display = ['id', 'ctext', 'final']