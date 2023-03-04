from django.shortcuts import render
from .models import client_info

# Create your views here.
def index(request):
    
    return render(request, 'sp/index.html')

def thankyou(request):
    
    return re
    