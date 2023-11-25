from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

class CustomUser(AbstractUser):
    is_artist=models.BooleanField(default=False)


class Profile(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='users/%Y', default='avatar.jpg')
    date_joined=models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering=['user']
        indexes=[
            models.Index(fields=['-user'])
        ]
    def __str__(self):
        return f'Profile of {self.user.username}'
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img=Image.open(self.photo.path)
        if img.height > 300 or img.width >300 :
            output_size=(300,200)
            img.thumbnail(output_size)
            img.save(self.photo.path)


