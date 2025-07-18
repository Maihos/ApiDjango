from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'description', 'created_at', 'updated_at', 'completed','is_deleted')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'updated_at', 'completed', 'is_deleted')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'completed')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

