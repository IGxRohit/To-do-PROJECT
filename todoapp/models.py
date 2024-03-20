from django.db import models

# Create your models here.
class todoR(models.Model):
    title=models.CharField(max_length=50)
    disc=models.TextField()
    tododone = models.BooleanField(default = False)
    dt= models.DateTimeField(auto_now_add=True,blank = True)