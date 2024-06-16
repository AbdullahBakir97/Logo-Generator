# logo_generator/models.py
from django.db import models
from django.contrib.auth.models import User

class UserLogoPreferences(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    color_choice = models.CharField(max_length=50)
    text_input = models.CharField(max_length=255)
    shape_choice = models.CharField(max_length=50)

    def __str__(self):
        return f"Preferences for {self.user.username}"
