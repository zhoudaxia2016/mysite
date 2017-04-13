from django.db import models

# Create your models here.
class Tag(models.Model):
  name = models.CharField(max_length=10)

  def __str__(self):
    return self.name
    
class Family(models.Model):
  name = models.CharField(max_length=10)
  title = models.CharField(max_length=30)

  def __str__(self):
    return self.name



class Post(models.Model):
  title = models.CharField(max_length=30)
  publish_time = models.DateTimeField('Date Published')
  intro = models.TextField()
  view = models.IntegerField(default=0)
  tags = models.ManyToManyField(Tag)
  family = models.ForeignKey(Family,null=True)

class Demo(Post):
  source = models.CharField(max_length=120)
  result = models.CharField(max_length=120)

  def __str__(self):
    return 'Demo: %s' %self.title

class Blog(Post):
  content = models.TextField()

  def __str__(self):
    return 'Blog: %s' %self.title

