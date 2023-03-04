from django.shortcuts import render
from spapp.models import clientinfo

# Create your views here.
def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        phone = request.POST['phone']
        pwd = request.POST['pwd1']
        Confirmpwd = request.POST['pwd2']
        message = request.POST['msg']
        submittedInfo = clientinfo.objects.create(email = email, phone = phone, pwd = pwd, Confirmpwd = Confirmpwd, message = message)
        submittedInfo.save()
    return render(request, 'SPapp/index.html')
    