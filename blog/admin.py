from django.contrib import admin
from .models import Blog, Keyword


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
        'image',
    )

    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Blog, BlogAdmin)
admin.site.register(Keyword)
