from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'temp2/index.html')

def doc(request):
    return render(request,'temp1/doc.html')