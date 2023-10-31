from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from history.models import Trade


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='Bitcoin.svg.png', upload_to='profile_images')
    win_rate = models.FloatField(default=0.0)
    bio = models.TextField()

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 200 or img.width > 200:
            new_img = (200, 200)
            img.thumbnail(new_img)
            img.save(self.image.path)