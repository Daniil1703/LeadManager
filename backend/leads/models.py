from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Lead(models.Model):
    name = models.CharField(_("Имя"), max_length=30)
    email = models.EmailField(_("Email"), max_length=30, unique=True)
    message = models.CharField(_("Сообщение"), max_length=500, blank=True)
    created_at = models.DateTimeField(_("Создано"), auto_now_add=True)
