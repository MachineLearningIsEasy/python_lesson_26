from django.core.management.base import BaseCommand
from articles.models import Article, Tag
from django.db.models import F


class Command(BaseCommand):

    def handle(self, *args, **options):

        #articles = Article.objects.all()
        # for article in articles:
        #     article.article_rating+=1
        #     article.save()
        #articles.update(article_rating = F('article_rating')+1)
        Article.objects.all().update(article_rating = F('article_rating')+1)