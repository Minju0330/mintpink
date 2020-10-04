from django.db import models

# Create your models here.

class Quest(models.Model):
  content = models.TextField()
  answer1 = models.CharField(max_length=200)
  answer2 = models.CharField(max_length=200)

  def __str__(self):
    return self.content


class Fairy(models.Model):
  code = models.IntegerField(null=False)
  character = models.CharField(max_length=200)
  explain = models.TextField()

  def __str__(self):
    return self.character