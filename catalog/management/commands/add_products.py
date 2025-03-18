from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Add test products to the database from fixture'

    def handle(self, *args, **kwargs):

        Category.objects.all().delete()
        Product.objects.all().delete()

        call_command('loaddata', 'categories_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully test categories to the database from fixture'))
        call_command('loaddata', 'products_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully test products to the database from fixture'))