from django.db import models


class Article(models.Model):
    titel = models.CharField(max_length = 100)
    slug =models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    # in add thumbnail
    # add in author
    def __str__(self):
        return self.titel

    def snippet(self):
        return self.body[0:50] + '.....'
