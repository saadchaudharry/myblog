from django.db import models
from django.db.models.signals import pre_save
from myblog.utils import *
# Create your models here.
class BlogPost(models.Model):
    title =models.CharField(max_length=120)
    slug =models.CharField(max_length=120,blank=True,null=True)
    image =models.ImageField(null=True,blank=True)
    message =models.TextField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-timestamp']

def slugfordetail(instance,sender,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

pre_save.connect(slugfordetail,sender=BlogPost)
