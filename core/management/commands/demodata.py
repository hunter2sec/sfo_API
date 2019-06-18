"""Initialize stock users"""
from django.core.management import BaseCommand, call_command

from core.models import Item
from django.contrib.auth import get_user_model
User = get_user_model()

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        call_command('loaddata', 'users', verbosity=0)
        for user in User.objects.all():
            user.save()

        call_command('loaddata', 'items', verbosity=0)
        for user in Item.objects.all():
            user.save()