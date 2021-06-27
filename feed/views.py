from django.shortcuts import render
from main.models import Organization
# Create your views here.
def main_page(request):
    username=request.user.username
    return render(request,"feed/main_page.html",{"username":username})

def humanities(request):
    organizations=Organization.objects.filter(category="HUMANITIES")
    return render(request,'feed/category.html',{'title':'Humanities','organizations':organizations})

def education(request):
    organizations=Organization.objects.filter(category="EDUCATION")
    return render(request,'feed/category.html',{'title':'Education','organizations':organizations})

def environment(request):
    organizations=Organization.objects.filter(category="ENVIRONMENT")
    return render(request,'feed/category.html',{'title':'Environment','organizations':organizations})

def health(request):
    organizations=Organization.objects.filter(category="HEALTH")
    return render(request,'feed/category.html',{'title':'Health','organizations':organizations})

def charity(request):
    organizations=Organization.objects.filter(category="CHARITY")
    return render(request,'feed/category.html',{'title':'Charity','organizations':organizations})

def religion(request):
    organizations=Organization.objects.filter(category="RELIGION")
    return render(request,'feed/category.html',{'title':'Religion','organizations':organizations})

def services(request):
    organizations=Organization.objects.filter(category="SERVICES")
    return render(request,'feed/category.html',{'title':'Services','organizations':organizations})

def other(request):
    organizations=Organization.objects.filter(category="OTHER")
    return render(request,'feed/category.html',{'title':'Other','organizations':organizations})