"""Posts admin panel."""
from django.contrib import admin

from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    """Posts admin panel configuration."""

    list_display = (
        'pk',
        'pub_date',
        'author',
        'group',
        'image',
    )
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    """Group admin panel configuration."""

    list_display = ('title', 'slug')


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
