from django.db import models

class logoModel(models.Model):
    lightLogo = models.ImageField( upload_to='images/logo',blank=True,null=True)

class HomeModel(models.Model):
    slider1 = models.ImageField( upload_to='images/profile_pics',blank=True,null=True)
    slider2 = models.ImageField( upload_to='images/profile_pics',blank=True,null=True)
    slider3 = models.ImageField( upload_to='images/profile_pics',blank=True,null=True)
    slider4 = models.ImageField( upload_to='images/profile_pics',blank=True,null=True)
    slider5 = models.ImageField( upload_to='images/profile_pics',blank=True,null=True)
    image1 = models.ImageField( upload_to='images/profile_pics',blank=True,null=True)
    image2 = models.ImageField( upload_to='images/profile_pics',blank=True,null=True)
    image3 = models.ImageField( upload_to='images/profile_pics',blank=True,null=True)


class AboutUs(models.Model):
    title = models.CharField(max_length=200,blank=True,null=True)
    image = models.ImageField( upload_to='images/about',blank=True,null=True)
    p1 = models.TextField(blank=True,null=True)
    p2 = models.TextField(blank=True,null=True)
    p3 = models.TextField(blank=True,null=True)
    p4 = models.TextField(blank=True,null=True)
    p5 = models.TextField(blank=True,null=True)
  
class Process(models.Model):
    heading1 = models.TextField(blank=True,null=True)
    heading2 = models.TextField(blank=True,null=True)
    heading3 = models.TextField(blank=True,null=True)
    image1 = models.ImageField( upload_to='images/process',blank=True,null=True)
    image2 = models.ImageField( upload_to='images/process',blank=True,null=True)
    image3 = models.ImageField( upload_to='images/process',blank=True,null=True)
    image4= models.ImageField( upload_to='images/process',blank=True,null=True)
    image5 = models.ImageField( upload_to='images/process',blank=True,null=True)
    image6 = models.ImageField( upload_to='images/process',blank=True,null=True)
    p1 = models.TextField(blank=True,null=True)
    p2 = models.TextField(blank=True,null=True)
    p3 = models.TextField(blank=True,null=True)
    p4 = models.TextField(blank=True,null=True)
    p5 = models.TextField(blank=True,null=True)
    p6 = models.TextField(blank=True,null=True)




class ContactUs(models.Model):
    email = models.CharField(max_length=200,blank=True,null=True)
    phone = models.CharField(max_length=200,blank=True,null=True)
    address = models.CharField(max_length=200,blank=True,null=True)


class Manufactormodel(models.Model):
    image1 = models.ImageField( upload_to='images/manufacctor',blank=True,null=True)
    image2 = models.ImageField( upload_to='images/manufacctor',blank=True,null=True)
    image3 = models.ImageField( upload_to='images/manufacctor',blank=True,null=True)

class SocialMedia(models.Model):
    facebook = models.CharField(max_length=200,blank=True,null=True)
    insta = models.CharField(max_length=200,blank=True,null=True)
    whatsapp = models.CharField(max_length=200,blank=True,null=True)