from django.shortcuts import render
from healthapp.models import *
# Create your views here.
def home(request):
    return render(request, 'index.html')

def starter(request):
    return render(request, 'starter-page.html')

def About(request):
    return render(request, 'About.html')

def appointment(request):
    if request.method == 'POST':

        all = Myappointment(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            datetime=request.POST['datetime'],
            department=request.POST['department'],
            doctor=request.POST['doctor'],
            message=request.POST['message']
        )
        all.save()
        return render(request, 'appointment.html')
    else:
        return render(request, 'appointment.html')


def show(request):
   allapointments = Myappointment.objects.all()
   return render(request, 'show.html', {'appointments': allapointments})