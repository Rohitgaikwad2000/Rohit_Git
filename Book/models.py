from django.db import models
from django.contrib.auth.models import User
 
# Create your models here.

class CustomBookManager(models.Manager):         # get active objects
    def get_active_objects(self):
        return self.filter(isdeleted=False)


    def get_inactive_objects(self):               # get in-active objects        
        return self.filter(isdeleted=True)
    
        
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    publication_date = models.DateField()
    isdeleted = models.BooleanField(default=False)
    price = models.IntegerField()
    objects = CustomBookManager()
    # created_by = models.ForeignKey(User,on_delete=models.CASCADE)
             

    def __str__(self):
        return f"{self.title}"
    

    class Meta:
        db_table = "Book"

      

class FileUpload(models.Model):
    name = models.CharField(max_length=100)
    uploaded_file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "file_upload"





class name(models.Model):
    name = models.CharField(max_length=12)
    company = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "Name"


