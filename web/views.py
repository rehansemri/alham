from django.shortcuts import render
from .models import HomeModel,logoModel,AboutUs,Process,ContactUs,Manufactormodel,SocialMedia
def home(request):

    imgaes= HomeModel.objects.first()
    logo = logoModel.objects.first() 
    socialMe = SocialMedia.objects.first()
    return render(request,'index.html',{"images":imgaes,"logo":logo,"social":socialMe})

def contact(request):
    logo = logoModel.objects.first() 
    contact= ContactUs.objects.first()
    socialMe = SocialMedia.objects.first() 
    print(contact.address)
    return render(request,'contact.html',{"logo":logo,"contactdata":contact,"social":socialMe})

def about(request):
    logo = logoModel.objects.first() 
    about= AboutUs.objects.first()
    socialMe = SocialMedia.objects.first()
    return render(request,'about.html',{"logo":logo,"about":about,"social":socialMe})

def manufactor(request):
    logo = logoModel.objects.first()
    manufactorData= Manufactormodel.objects.first() 
    socialMe = SocialMedia.objects.first()
    return render(request,'manufacture.html',{"logo":logo,"manufactordata":manufactorData,"social":socialMe})
def process(request):
    logo = logoModel.objects.first() 
    process= Process.objects.first()
    socialMe = SocialMedia.objects.first()
    return render(request,'Process.html',{"logo":logo,"process":process,"social":socialMe})