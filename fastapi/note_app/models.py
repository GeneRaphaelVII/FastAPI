from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, related_name='notes', blank=True)

    def __str__(self):
        return self.title
