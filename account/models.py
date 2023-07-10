from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True, help_text='Format date: YYYY-mm-dd, between 6 and 94 years')

    def __str__(self):
        return f"Profile for user {self.user.username}"