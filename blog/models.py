from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    context = models.CharField(max_length=2050)
    slug = models.SlugField(max_length=250)

    def __str__(self) -> str:
        return self.title
