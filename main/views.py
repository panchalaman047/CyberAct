from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import SignUpOrganization
from .models import Organization

# Create your views here.
def starting_page(request):
    return render(request,"main/starting_page.html",{})

def organization(request):
    if request.method == "POST":
        form=SignUpOrganization(request.POST)
        if form.is_valid():
            n=form.cleaned_data['name']    
            c=form.cleaned_data['Category']
            d=form.cleaned_data['description']
            t=Organization( name =n, category =c,description =d)
            t.save()
        return HttpResponseRedirect('/')
    else:
        form=SignUpOrganization()
    return render(request,"main/signuporganization.html",{"form":form})