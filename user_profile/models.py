from django.db import models
from django.contrib.auth.models import User
from PIL import Image


 # Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return str(self.user)

    # def save(self):
    #     super().save()
    #
    #     img = Image.open(self.avatar.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)