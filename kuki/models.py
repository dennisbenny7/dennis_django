from django.db import models
# from profiles.models import Profile
from django.urls import reverse
from django.contrib.auth.models import User



class Report(models.Model):
    name = models.CharField(max_length=120)
    user = models.CharField(max_length=120,null=True,unique=False,blank=True)
    image = models.ImageField( blank=True, default=None)
    remarks = models.TextField()
    bio = models.TextField(default="no bio...")
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    intrest=models.CharField(max_length=120,null=True)

    # def get_absolute_url(self):
    #     return reverse('reports:detail', kwargs={'pk': self.pk})
    # def save(self,*args,**kwargs):
        

                
            
    #    
    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ('-created',)

# Create your models here.
class Profile(models.Model):

    hai=models.CharField(max_length=120,null=True,blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="no bio...")
    avatar = models.ImageField(upload_to='avatars',default="avatars/klc.jpg")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
  
    def save(self,*args,**kwargs):
        self.hai=self.user.username

  
        return super().save(*args,**kwargs)

    def __str__(self):
        return f"Profile of {self.user.username}"

