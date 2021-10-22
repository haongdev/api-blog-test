from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField(max_length=500)
    content = models.TextField()

    def __str__(self):
        return self.title
