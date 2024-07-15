from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


# MyUserManager class is a custom user manager for creating regular and superuser accounts.
class MyUserManager(BaseUserManager):
    # Method to create a regular user account.
    def create_user(self, first_name, last_name, username, email, password=None):
        # Check if an email is provided.
        if not email:
            raise ValueError('Users must have an email address')

        # Check if a username is provided.
        if not username:
            raise ValueError('Users must have an username')

        # Create a new user instance with the provided details.
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email),  # Normalize the email by lowercasing the domain part.
        )

        # Set the password for the user, which hashes it before storing.
        user.set_password(password)

        # Save the user instance to the database.
        user.save(using=self._db)
        return user

    # Method to create a superuser account.
    def create_superuser(self, first_name, last_name, username, email, password):
        # Use the create_user method to create a base user with the provided details.
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )

        # Set the superuser specific flags.
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True

        # Save the superuser instance to the database.
        user.save(using=self._db)
        return user


# Account class defines the custom user model extending AbstractBaseUser.
class Account(AbstractBaseUser):
    # Basic user fields.
    first_name = models.CharField(max_length=50)  # First name of the user.
    last_name = models.CharField(max_length=50)  # Last name of the user.
    username = models.CharField(max_length=50, unique=True)  # Unique username for the user.
    email = models.EmailField(max_length=100, unique=True)  # Unique email address for the user.
    phone = models.CharField(max_length=20)  # Phone number for the user, not necessarily unique.

    # System managed fields.
    date_joined = models.DateTimeField(auto_now_add=True)  # Date and time when the account was created.
    last_login = models.DateTimeField(auto_now=True)  # Date and time of the last login. Updates on each login.
    is_admin = models.BooleanField(default=False)  # Flag indicating if the user has admin rights.
    is_staff = models.BooleanField(default=False)  # Flag indicating if the user is a staff member.
    is_active = models.BooleanField(default=False)  # Flag indicating if the user's account is active.
    is_superuser = models.BooleanField(default=False)  # Flag indicating if the user is a superuser.

    # Defines the field used as the unique identifier for the user during authentication.
    USERNAME_FIELD = 'email'

    # Additional fields required when creating a user via the command line or admin interface.
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    # Link the custom user manager to the Account model.
    objects = MyUserManager()

    # String representation of the user.
    def __str__(self):
        return self.email  # Returns the email address as the representation of the user.

    # Custom permission method to check if the user has a specific permission.
    def has_perm(self, perm, obj=None):
        return self.is_admin  # For simplicity, return True if the user is an admin.

    # Custom method to check if the user has permissions to access the app.
    def has_module_perms(self, app_label):
        return True  # By default, return True indicating access to any app.

