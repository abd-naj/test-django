import logging

from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import  HotelForm
from .models import Login, Personal, Contact, Academy, Wishlist, Document

# Create your views here.
logger = logging.getLogger('app_api')  # from LOGGING.loggers in settings.py


def personal(request):
    logger.info('personal')
    if request.method=="POST":
        name = request.POST.get('name')
        placeofpirth = request.POST.get('placeofpirth')
        ratio = request.POST.get('ratio')
        dataofbirth = request.POST.get('dataofbirth')
        namefather = request.POST.get('namefather')
        gender = request.POST.get('gender')
        mothername = request.POST.get('mothername')
        status = request.POST.get('status')
        data = Personal( name=name ,placeofpirth=placeofpirth ,ratio=ratio ,dataofbirth=dataofbirth ,
        namefather=namefather ,gender=gender ,mothername=mothername ,status=status)
        data.save()
        return redirect('contact')

    return render(request, "pages/personal.html")

def contact(request):
    if request.method=="POST":
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        name = request.POST.get('name') 
        website = request.POST.get('website')
        message = request.POST.get('message')
        x = Contact(phone=phone ,email=email ,name=name ,website=website ,message=message )
        x.save()

    return render(request, "pages/contact.html")

def academy(request):
    if request.method=="POST":
        elementaryschool = request.POST.get('elementaryschool')
        certificatedate = request.POST.get('certificatedate')
        preparatoryschool = request.POST.get('preparatoryschool')
        modified = request.POST.get('modified')
        highschool = request.POST.get('highschool')
        certificatesource = request.POST.get('certificatesource')
        data = Academy(elementaryschool=elementaryschool ,certificatedate=certificatedate ,preparatoryschool=preparatoryschool ,modified=modified,highschool=highschool ,certificatesource=certificatesource)
        data.save()
    return render(request, "pages/academy.html")

# def document(request):
#     if request.method=="POST":
#         imgper = request.POST.get('imgper')
#         imgid = request.POST.get('imgid')
#         imgcer = request.POST.get('imgcer')
#         data = Document(imgper=imgper ,imgid=imgid ,imgcer=imgcer)
#         data.save()
#
#     return render(request, "pages/document.html")

def wishlist(request):
    if request.method=="POST":
        name = request.POST.get('name') 
        placeofbirth = request.POST.get('placeofbirth')
        firstwish = request.POST.get('firstwish')
        ratio = request.POST.get('ratio')
        dateofbirth = request.POST.get('dateofbirth')
        secondwish = request.POST.get('secondwish')
        fathersnameandlineage = request.POST.get('fathersnameandlineage')
        gender = request.POST.get('gender')
        thirdwish = request.POST.get('thirdwish')
        mothersnameandlineage = request.POST.get('mothersnameandlineage')
        status = request.POST.get('status')
        fourthwish = request.POST.get('fourthwish')
        data = Wishlist(name=name ,placeofbirth=placeofbirth ,firstwish=firstwish ,ratio=ratio ,dateofbirth=dateofbirth ,secondwish=secondwish ,fathersnameandlineage=fathersnameandlineage ,gender=gender ,thirdwish=thirdwish ,mothersnameandlineage=mothersnameandlineage ,status=status ,fourthwish=fourthwish)
        data.save()

    return render(request, "pages/wishlist.html")  

def sgnin(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']
        data = Login(email=email, password=password)
        data.save()

    return render(request, "pages/sgnin.html") 

def students(request):
    
    return render(request, 'pages/students.html',  {'namestudents':Personal.objects.all()})   

def studentsdesirs(request):

    return render(request, 'pages/studentsdesirs.html',  {'wishlists':Wishlist.objects.all()})

# Create your views here.
def document(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('document')
    else:
        form = HotelForm()
    return render(request, 'pages/document.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')