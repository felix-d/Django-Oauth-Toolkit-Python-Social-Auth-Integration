from django.db import models


# Create your models here.
class Beer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    brand = models.CharField(max_length=100, default='')
    beer_type = models.CharField(max_length=100, default='')
    ml = models.IntegerField(default=330)
    owner = models.ForeignKey('auth.User', related_name="beers")

    class Meta:
        ordering = ('created',)
