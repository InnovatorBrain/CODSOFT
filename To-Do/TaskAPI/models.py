from django.db import models

# Create your models here.

class Task(models.Model):
  title = models.CharField(max_length=250)
  description = models.TextField(null=True, blank=True)
  completed = models.BooleanField(default=False, blank=True, null=True)
      
  def __str__(self) -> str:
    return self.title
  
  class Meta:
    ordering = ['title']
  
