from django.db import models


class File(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title
