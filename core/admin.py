from django.contrib import admin

from core.models import File


class FileAdmin(admin.ModelAdmin):
    list_display = ["title", "image", "description"]


admin.site.register(File, FileAdmin)
