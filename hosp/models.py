from django.db import models

# Create your models here.
class tbl_doctor(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    specilization=models.CharField(max_length=100)
    experience=models.IntegerField()
    salary=models.IntegerField()
    class Meta:
        db_table="tbl_doctor"
class tbl_nurse(models.Model):  
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    qualification=models.CharField(max_length=100)
    experience=models.IntegerField()
    salary=models.IntegerField()
    class Meta:
        db_table="tbl_nurse"




