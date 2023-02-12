from django.db import models

# Create your models here.
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, Permission, PermissionsMixin
from django.db import models

from django.utils import timezone
from django.utils.translation import gettext_lazy as _



class SimpleUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('User must have an email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.is_active = True
        user.is_staff = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class Employee(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=200, null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    email_verified = models.BooleanField(default=False)
    email_bounced = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = SimpleUserManager()

    class Meta:
        verbose_name = _('employee')
        verbose_name_plural = _('employees')

    def get_full_name(self):
        return f'{self.first_name or ""} {self.last_name or ""}'

    @property
    def full_name(self):
        return f'{self.first_name or ""} {self.last_name or ""}'

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email


