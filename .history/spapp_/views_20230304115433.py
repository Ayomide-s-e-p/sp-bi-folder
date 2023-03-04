from django.shortcuts import render
from .models import client_info

# Create your views here.
def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        phone = request.POST['phone']
        pwd = request.POST['pwd1']
        Confirmpwd = request.POST['pwd2']
        message = request.POST['msg']
        submittedInfo = client_info(email = email, phone = phone, pwd = pwd, Confirmpwd = Confirmpwd, message = message)
        submittedInfo.save()
    return render(request, 'sp/index.html')

def thankyou
    