from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from user.models import Catgeories

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True,null=True)
    date_time = models.DateTimeField(default=timezone.now)
    # category = models.ForeignKey(Catgeories,on_delete=models.CASCADE,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)


    class Meta:
        db_table = 'post'




