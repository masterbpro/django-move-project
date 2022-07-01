from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='movie')
    kinopoisk_id = models.IntegerField(null=False)

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'

    def __str__(self):
        return self.name
