from django.db import models
from django.utils import timezone



# Create your models here.


class Post(models.Model):
    post_title = models.CharField(max_length=200)
    body = models.TextField()
    create_at = models.DateTimeField('date created')

    def __str__(self):
        return self.post_title


