import random

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

GENDER_TYPE = (
    ("0", "선택안함"),
    ("1", "남자"),
    ("2", "여자"),
)

class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    object = CustomUserManager()
    
    phone_number = models.CharField(max_length=16, default='0')
    gender = models.CharField(max_length=8, choices=GENDER_TYPE, default=0)

    def __str__(self):
        return self.phone_number

    class Meta:
        db_table = "users"