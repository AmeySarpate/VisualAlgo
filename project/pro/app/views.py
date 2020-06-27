from django.shortcuts import render

# Create your views here.

def home(request):
    col=70;
    row=35;
    return render(request,'home.html',{'rows':range(1,row+1),'cols':range(1,col+1),'nrows':row,'ncols':col})


def side(request):
    return render(request,'side.html');
