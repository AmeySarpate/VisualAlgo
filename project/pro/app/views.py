from django.shortcuts import render

# Create your views here.

def home(request):

    # prev valuse was 70 and 30
    col=61;
    row=21;
    return render(request,'home.html',{'rows':range(1,row+1),'cols':range(1,col+1),'nrows':row,'ncols':col})


def side(request):
    return render(request,'side.html');
