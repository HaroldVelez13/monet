from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils import timezone


class Command(BaseCommand):
    help = 'Monet init'

    def handle(self, *args, **options):
        create_super_user()


def create_super_user():
    User = get_user_model()
    username = 'monet_admin'
    password = 'secretadmin1234'
    email = 'admin@monet.com'

    if User.objects.filter(username=username).exists():
        return

    last_login = timezone.now()
    User.objects.create_superuser(
        username=username, password=password, email=email, last_login=last_login)
