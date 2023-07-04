from django.db import models
from datetime import datetime 

class StatusTable(models.Model):
    TagStatus=models.CharField(max_length=50)
    NameOfDevice=models.CharField(max_length=50)
    TimeIs=models.DateTimeField(default=datetime.now,blank=False)



class StatusTabletwo(models.Model):
    TagStatus8192=models.CharField(max_length=50)
    TagStatus8193=models.CharField(max_length=50)
    TagStatus8194=models.CharField(max_length=50)
    TagStatus8195=models.CharField(max_length=50)
    TagStatus8196=models.CharField(max_length=50)
    TagStatus8197=models.CharField(max_length=50)
    TagStatus8198=models.CharField(max_length=50)
    TagStatus8199=models.CharField(max_length=50)
    
    TimeIs=models.DateTimeField(default=datetime.now,blank=False)



class Emailtable(models.Model):
    EmailInModel=models.EmailField(max_length=100)
    
    


class StatusTable8192(models.Model):
    TagStatus=models.CharField(max_length=50)
    NameOfDevice=models.CharField(max_length=50)
    TimeIs=models.DateTimeField(default=datetime.now,blank=False)
    
    
    
    
    
class StatusTable8193(models.Model):
    TagStatus=models.CharField(max_length=50)
    NameOfDevice=models.CharField(max_length=50)
    TimeIs=models.DateTimeField(default=datetime.now,blank=False)
   
   
class StatusTable8194(models.Model):
    TagStatus=models.CharField(max_length=50)
    NameOfDevice=models.CharField(max_length=50)
    TimeIs=models.DateTimeField(default=datetime.now,blank=False)        
    
    
class StatusTable8195(models.Model):
    TagStatus=models.CharField(max_length=50)
    NameOfDevice=models.CharField(max_length=50)
    TimeIs=models.DateTimeField(default=datetime.now,blank=False)      
    
    
class StatusTable8196(models.Model):
    TagStatus=models.CharField(max_length=50)
    NameOfDevice=models.CharField(max_length=50)
    TimeIs=models.DateTimeField(default=datetime.now,blank=False)           
    
class StatusTable8197(models.Model):
    TagStatus=models.CharField(max_length=50)
    NameOfDevice=models.CharField(max_length=50)
    TimeIs=models.DateTimeField(default=datetime.now,blank=False)       
    
    
    
class StatusTable8198(models.Model):
    TagStatus=models.CharField(max_length=50)
    NameOfDevice=models.CharField(max_length=50)
    TimeIs=models.DateTimeField(default=datetime.now,blank=False)               