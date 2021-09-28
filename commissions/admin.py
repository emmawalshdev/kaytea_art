from django.contrib import admin
from .models import Commissions


class CommissionsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'image',
    )


# Register your models here.
admin.site.register(Commissions, CommissionsAdmin)
