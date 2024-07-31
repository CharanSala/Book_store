# views.py
import razorpay
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .models import image,document,Register,user_info
from django.contrib import messages
from django.http import HttpResponse
client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
global login
login=False
current_user=""
def home(request):
    documents = image.objects.all()
    context = {
        'documents': documents
    }
    return render(request, 'home.html', context)

def book1(request, name):
    paid=False
    mybook = get_object_or_404(document, title=name)
    if login==True:
        info=user_info.objects.filter(user_email=current_user)
        if info:
            for i in info:
                if i.book_title==name:
                    paid=True
        if paid !=True:
            amount = 500  # Amount in paise (5 INR)
            order = client.order.create({
            'amount': amount,
            'currency': 'INR',
            'payment_capture': '1'
            })
            context = {
                'mybook': mybook,
                'order_id': order['id'],
                'razorpay_key_id': settings.RAZORPAY_KEY_ID,
                'amount': amount
            }

            return render(request, 'payment.html', context)
        else:
            return render(request, 'mybook.html', {'mybook': mybook})
    else:
        return redirect('register')

def payment_success(request, name):
    mybook = get_object_or_404(document, title=name)
    mybook.is_paid = True
    mybook.save()
    book_info=user_info(user_email=current_user,book_title=name)
    book_info.save()
    return redirect('book1_url', name=name)
def register(request):
    return render(request,'register.html')
def submit(request):
    visible=False
    if request.method == 'POST':
        username=request.POST.get('username')
        email = request.POST.get('mymail')
        password = request.POST.get('mypassword')
        alldata=Register.objects.all()
        for i in alldata:
            if i.email==email:
                visible=True
        if visible == False:
            data = Register(username=username,email=email, password=password)
            data.save()
            messages.success(request, 'User registered successfully')
        else:
            messages.warning(request, 'User already exists')
    return redirect('home')
def login(request):
    return render(request,'login.html')
def check_login(request):
    global login,current_user
    login=False
    check_email=request.POST.get('loginemail')
    check_password=request.POST.get('loginpassword')

    mydata=Register.objects.all()
    for i in mydata:
        if i.email==check_email:

            if i.password==check_password:
                login=True
                mydata=Register.objects.filter(email=check_email)
                current_user=check_email
                documents=image.objects.all()
                return render(request,'loginhome.html',{'mydata':mydata,'documents':documents})

    if login==False:
        messages.warning(request, 'Please check your email and password')
        return redirect('home')
def logout(request):
    global login
    login=False
    documents=image.objects.all()
    return render(request,'home.html',{'documents':documents})
def history(request):
    mydata=Register.objects.filter(email=current_user)
    book_history=user_info.objects.filter(user_email=current_user)
    return render(request,'history.html',{'mydata':mydata,'book_history':book_history})
def login_home(request):
    mydata=Register.objects.filter(email=current_user)
    documents=image.objects.all()
    return render(request,'loginhome.html',{'mydata':mydata,'documents':documents})
