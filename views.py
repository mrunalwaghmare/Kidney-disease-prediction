from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# import csv
# import os
from django.shortcuts import redirect, render, get_object_or_404
from .models import Member
from .forms import MemberForm


def register(request):
    if request.method == 'POST':
        form =RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('login_view')
        
    else:
        form = RegisterForm()
    return render(request,'register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('kidney')
            
    else:
            form = AuthenticationForm()
    return render(request, 'login.html',{'form':form})

# def home(request):
#     return render(request ,'home.html')

def result(request):
    if request.method == 'POST':
        # Handle form submission
        # Extract form data from request.POST

        gravity = request.POST.get('gravity')
        pH = request.POST.get('pH')
        osmo = request.POST.get('osmo')
        cond = request.POST.get('cond')
        urea = request.POST.get('urea')
        calc = request.POST.get('calc')
       
        lis = [gravity,pH,osmo,cond,urea,calc]
        print(lis)

        #training model
        from joblib import load
        model = load("D:/class proj/KIDNEY STONES/modelkse.joblib")

        #make prediction
        result = model.predict([lis])
        print(lis)

        if result[0]==0:
            print("No")
            value = 'Negative'

        else:
            print("Yes")
            value = 'Positive'


        return render(request, 'result.html', {
                    'ans':value,
                    'title':'Predict',

    })

        # Process the data as needed
        # For now, just returning a simple HttpResponse
        # return HttpResponse(f"Received: Glucose: {glucose}, Blood Pressure: {blood_pressure}, Skin Thickness: {skin_thickness}, Insulin: {insulin}, BMI: {bmi}, Diabetes Pedigree Function: {diabetes_pedigree_function}, Age: {age}")

def kidney(request):
    return render(request,"kidney.html")

def start(request):
    return render(request,"start.html")

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

#for add.html
def add(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indexx')
    else:
        form = MemberForm()
    return render(request,'add.html',{'form':form})

#for indexx.html
def indexx(request):
    mem = Member.objects.all()
    return render(request,'indexx.html',{'mem':mem})

def update(request ,id):
    mem = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        form = MemberForm(request.POST,instance=mem)
        if form.is_valid():
            form.save()
            return redirect('indexx')
    else:
        form = MemberForm(instance=mem)
    return render(request, 'update.html',{'form':form})


def delete(request, id):
    mem = get_object_or_404(Member, id=id)
    mem.delete()
    return redirect('indexx')


def filter_details(request):
    mem = Member.objects.all()

    #filtering logic
    firstname_query = request.GET.get('firstname')
    lastname_query = request.GET.get('lastname')
    country_query = request.GET.get('country')

    if firstname_query:
        mem = mem.filter(firstname__icontains=firstname_query)
    if lastname_query:
        mem = mem.filter(lastname__icontains=lastname_query)
    if country_query:
        mem =mem.filter(country__icontains=country_query)   

    return render(request,'filter_details.html',{'mem':mem})     
        
        # def login_required(login_url)

def logout1(request):
    logout(request)
    messages.success(request,"Logged out successful")
    return redirect('home')


    






