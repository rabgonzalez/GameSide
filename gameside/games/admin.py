from django.contrib import admin

from .models import *


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'slug',
        'description',
        'cover',
        'price',
        'stock',
        'released_at',
        'pegi',
    )
    search_fields = (
        'pk',
        'title',
        'slug',
        'description',
        'cover',
        'price',
        'stock',
        'released_at',
        'pegi',
    )
    list_filter = ('title',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating', 'comment', 'created_at', 'updated_at')
    search_fields = ('id', 'rating', 'comment', 'created_at', 'updated_at')
    list_filter = ('id',)
