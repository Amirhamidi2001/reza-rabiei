from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """
    This class is for django administration
    """

    date_hierarchy = "created_at"
    list_display = ("name", "email")
    list_filter = ("email",)
    search_fields = ("name", "message")


admin.site.register(Contact, ContactAdmin)