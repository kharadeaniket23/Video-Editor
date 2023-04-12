from django.shortcuts import render
from .models import APPEDI
# Create your views here.
def index(request):
    video=APPEDI.objects.all()
    return render(request,"index.html",{"video":video})

