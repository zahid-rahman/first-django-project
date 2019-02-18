from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True,null=True)
    date_time = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        db_table = 'post'

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return self.user.username+'\'s profile'

    # def save(self):
    #     super().save()

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)