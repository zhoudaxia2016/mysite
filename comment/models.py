from django.db import models
from login.models import User

# Create your models here.
class Comment(models.Model):
  user = models.CharField(max_length=30)
  blog = models.IntegerField(id)
  publish_time = models.DateField(auto_now_add=True)
  content = models.TextField()

  def __str__(self):
    return self.content[:10]
