from django.db import models
from datetime import datetime


class Article(models.Model):
    title = models.CharField('Title', max_length=256, null=False)
    intro = models.CharField('Intro', max_length=256, null=False)
    text = models.TextField('Main text', null=False)
    date = models.DateTimeField('Date', default=datetime.utcnow)

    def __repr__(self):
        return self.title

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
