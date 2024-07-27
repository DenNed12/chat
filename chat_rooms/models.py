from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        app_label = 'chat_rooms'

    def __str__(self):
        return self.name