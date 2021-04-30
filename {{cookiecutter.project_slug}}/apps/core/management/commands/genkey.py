import secrets
import sys

from django.core.management import BaseCommand


def gen_key():
    """Generates a 32 bit hex key."""
    for x in range(1):
        key = secrets.token_hex(32)
        sys.stdout.write('Key ' + str(x+1) + ': ' + key + "\n")


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        gen_key()
