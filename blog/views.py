from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    
    context={"id":"1","name":"Abhinav Raj","dec":"The owner of this demo Webpage "}
    return render(request,'about.html',context)



def contact(request):
    return render(request,'contact.html')

def privacy(request):
    return render(request,'privacy.html')

def services(request):
    return render(request,'services.html')




