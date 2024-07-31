from django.db import models
import os
def filepath(request,filename):
    filename=filename
    return os.path.join('static/images/',filename)

def filepath2(request,filename):
    filename=filename
    return os.path.join('static/documents/',filename)

class image(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    image=models.ImageField(upload_to=filepath,null=True,blank=True)
    def __str__(self):
        return self.name

class document(models.Model):
    title=models.ForeignKey(image,on_delete=models.CASCADE,to_field='name')
    pdf=models.FileField(upload_to=filepath2)
    upload_at=models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
class Register(models.Model):
    username=models.CharField(max_length=255,null=True,blank=True)
    email=models.CharField(max_length=100,primary_key=True)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.email
class user_info(models.Model):
    user_email=models.CharField(max_length=100)
    book_title=models.CharField(max_length=255)
