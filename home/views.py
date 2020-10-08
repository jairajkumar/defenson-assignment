from django.shortcuts import render
from. models import Information


# Create your views here.

def home(request):
    if request.method== 'POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        date=request.POST['date']
        count=request.POST['count']
        radio = request.POST['exampleRadios']
        information = Information(name = name, phone = phone, email = email, address = address,date = date,count = count, radio = radio)
        information.save()
        print(name,email,phone,address,date,count,radio)
   
    return render(request,'home.html')

# Create your views here.
