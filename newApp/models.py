from django.db import models

# Create your models here.


class UserInfo(models.Model):
    name =models.CharField(max_length=100)
    class Meta:
        db_table = 'userinfo'
    def __str__(self):
        return self.name
    
class CRUDfunctions(models.Model):
    title=models.CharField(max_length=100)
    description= models.TextField()
    class Meta:
        db_table='crudfunction'
    def __str__(self):
        return self.title
        
        