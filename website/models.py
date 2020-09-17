from django.db import models


# Create your models here.
class Website(models.Model):
    title = models.CharField(max_length=1024)
    content = models.TextField(null=True, blank=True)
    link = models.TextField(null=True)
    has_visited = models.BooleanField(default=False)
    links_to = models.ManyToManyField('Website')
