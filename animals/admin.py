from django.contrib import admin

from animals.models import Animals


@admin.register(Animals)
class AnimalsAdmin(admin.ModelAdmin):
    readonly_fields = ("publish_date", "change_date", "likes")
    list_display = ("kind","name", "publish_date", "change_date", "author", "published")
    search_fields = ("kind", "name")
    list_filter = ("publish_date", "change_date", "published")
