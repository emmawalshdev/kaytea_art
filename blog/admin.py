from django.contrib import admin
from .models import Blog, Keyword, Reply


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
        'image',
    )

    list_filter = ('date',)


class ReplyAdmin(admin.ModelAdmin):
    list_display = (
        'blog',
        'author',
        'date',
    )
    list_filter = ('date',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Reply, ReplyAdmin)
admin.site.register(Keyword)
