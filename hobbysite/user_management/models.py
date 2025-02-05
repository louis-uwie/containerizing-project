from django.db import models
from django.contrib.auth.models import User

"""
default display_name is user.username
default email is user.email
these are provided in Django's default registration form
"""


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100, blank=True)
    display_picture = models.ImageField(
        upload_to="media/user_management/display_picture",
        blank=True,
        null=True
        )
    email = models.EmailField(blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        if not self.display_name:
            self.display_name = self.user.username
        if not self.email:
            self.email = self.user.email
        super().save(*args, **kwargs)
