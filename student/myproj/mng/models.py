from django.db import models

# Create your models here.
class department(models.Model):
     name=models.CharField(max_length=38)
     location=models.CharField(max_length=56)
     def __str__(self):
        return self.name
class role(models.Model):
     name=models.CharField(max_length=38)
     def __str__(self):
        return self.name
class employee(models.Model):
    first_name=models.CharField(max_length=34)
    last_name=models.CharField(max_length=34)
    dept=models.ForeignKey("department",on_delete=models.CASCADE)
    rol=models.ForeignKey("role",on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)   
    bonus=models.IntegerField(default=0)
    Phone_number=models.IntegerField(default=0)
    def __str__(self):
        return "%s%s%s"%(self.first_name,self.last_name,self.Phone_number)

