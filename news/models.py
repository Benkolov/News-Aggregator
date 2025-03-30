from django.db import models


class Headline(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null=True, blank=True)
    url = models.TextField()
    source = models.CharField(max_length=50, default='Unknown')

    def __str__(self):
        return self.title
