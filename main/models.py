from django.db import models

# Create your models here.

class StallRegistration(models.Model):
    stall_name = models.CharField(max_length=150)
    contact_person = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    cuisine_type = models.CharField(max_length=100, help_text="e.g., Chinese, Italian, Street Food, Beverages")
    stall_requirements = models.TextField(blank=True, null=True, help_text="e.g., 2 tables, 1 power outlet, space for deep fryer")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stall_name