from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=50)
    created_date=models.DateTimeField(auto_now_add=True)
    draft=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title