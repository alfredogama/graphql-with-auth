"""
Account models
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Model of custom user
    """

    email = models.EmailField(_("email address"), max_length=60, unique=True)
    first_name = models.CharField(_("first name"), max_length=28, blank=True)
    last_name = models.CharField(_("last name"), max_length=28, blank=True)
    registration_timestamp = models.DateTimeField(
        _("registration timestamp"), auto_now_add=True
    )
    is_active = models.BooleanField(_("active"), default=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def get_full_name(self):
        """
        Function to get the full name of the user
        :return: the first_name plus the last_name, with an space in between.
        """
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()

    def get_short_name(self):
        """
        Function to get only the first name of the user
        :return: short name for the user
        """
        return self.first_name
