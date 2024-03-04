from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone


class Color(models.Model):
    color = models.CharField(max_length = 128)
    
    def __str__(self):
        return self.color

class Diary(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE, null = True)
    title = models.CharField(max_length = 128, null = True) #charfield 純文字
    body = RichTextField(blank = True, null = True)
    created = models.CharField(default = timezone.now, max_length= 128) #because its only text, we can edit it and fix timezone problems
    color = models.ForeignKey(Color, on_delete = models.CASCADE, null = True)
    order = models. DateTimeField(auto_now_add = True, null = True) 

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-order']