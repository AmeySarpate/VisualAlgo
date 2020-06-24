from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html',{'rows':range(1,41),'cols':range(1,80)})


def side(request):
    return render(request,'side.html');
