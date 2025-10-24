from django.contrib import admin
from .models import StallRegistration

class StallRegistrationAdmin(admin.ModelAdmin):
    # What to show in the list view
    list_display = ('stall_name', 'contact_person', 'email', 'phone', 'cuisine_type', 'created_at')
    # What to allow searching by
    search_fields = ('stall_name', 'contact_person', 'email', 'cuisine_type')
    # What to allow filtering by
    list_filter = ('cuisine_type', 'created_at')

# Register your model with the custom admin class
admin.site.register(StallRegistration, StallRegistrationAdmin)