from django.db import models

# Create your models here.

class Fairy(models.Model):
  code = models.IntegerField(null=False)
  character = models.CharField(max_length=200)
  explain = models.TextField()

  def __str__(self):
        return self.character