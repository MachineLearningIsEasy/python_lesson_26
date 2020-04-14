from django.core.management.base import BaseCommand
from articles.models import Article, Tag
from mixer.backend.django import mixer

class Command(BaseCommand):

    def handle(self, *args, **options):
        article = mixer.cycle(100).blend(Article)