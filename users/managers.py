"""
Account managers
"""
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """
    Class to manage the user creation
    """

    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        """
        Function to create a user
        :param email: user's email
        :param password: user's password
        :param extra_fields: other fields
        :return: New user
        :raise: ValueError: Empty email field
        """
        if not email:

            raise ValueError("The given email must be set.")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Function to create a super user
        :param email: user's email
        :param password: user's password
        :param extra_fields: other fields
        :return: Function to create a new user
        :raise: ValueError: is_superuser boolean must be True
        """
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_superuser") is not True:

            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)
