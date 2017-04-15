from django.db import models

# Create your models here.
class Word(models.Model):
  user = models.CharField(max_length=30)
  publish_time = models.DateTimeField(auto_now_add=True)
  content = models.TextField()

  def __str__(self):
    return '%s留言于%s' %(self.user,self.publish_time)
