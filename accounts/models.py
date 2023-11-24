from django.db import models

# Create your models here.

class Movie(models.Model):
    cover_photo=models.ImageField(blank=True,null=False,upload_to='images/')
    name=models.CharField(max_length=255, null=True)
    slug=models.SlugField(max_length=255, null=True)
    precover=models.ImageField(blank=True,null=False,upload_to='images/')
    videos=models.FileField(blank=True,null=False,upload_to='video/')
    date_added= models.DateTimeField(auto_now_add=True)   
    
    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name


class Features(models.Model):
    cover_photo=models.ImageField(blank=True,null=False,upload_to='images/')
    name=models.CharField(max_length=255, null=True)
    slug=models.SlugField(max_length=255, null=True)
    precover=models.ImageField(blank=True,null=False,upload_to='images/')
    videos=models.FileField(blank=True,null=False,upload_to='video/')
    date_added= models.DateTimeField(auto_now_add=True)   
    
    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name