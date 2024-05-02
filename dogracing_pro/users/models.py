from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateField, EmailField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from datetime import date


class User(AbstractUser):
    """
    Default custom user model for Dogracing Pro.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=100)
    first_name = CharField(max_length=30, blank=True, default='Безымянный')
    last_name = CharField(max_length=30, blank=True, default='Пользователь')
    middle_name = CharField(max_length=30, null=True)
    telegram = CharField(max_length=30, blank=True)
    birthday = DateField(default=timezone.now, null=False)
    phone = CharField(max_length=30, blank=True)
    email = EmailField(null=False, blank=True)

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
