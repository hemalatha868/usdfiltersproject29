from django.shortcuts import render

# Create your views here.
def usd(request):
    d={'data':'Hai how are yOU'}
    return render(request,'usd.html',d)
