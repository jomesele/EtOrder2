from django.shortcuts import render,redirect
from accounts.forms import customerForm,customerAddForm,staffForm,staffAddForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from accounts.models import Customer,Staff 
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request,'accounts/index.html')

@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    return render(request,'accounts/register.html')

def registerCustomer(request):
    registered=False
    if request.method=='POST':
        var_customerForm=customerForm(request.POST)
        var_customerAddForm=customerAddForm(request.POST)
        if var_customerForm.is_valid() and var_customerAddForm.is_valid():
            customerprimary=var_customerForm.save()
            customerprimary.set_password(customerprimary.password)
            customerprimary.save()
            customerAdd=var_customerAddForm.save(commit=False)
            customerAdd.customer=customerprimary
            customerAdd.save()
            registered=True
    else:
        var_customerForm=customerForm()
        var_customerAddForm=customerAddForm()
    return render(request,'accounts/registerCustomer.html',{'var_customerForm':var_customerForm,'var_customerAddForm':var_customerAddForm,'registered':registered})


def registerStaff(request):
    registered=False
    if request.method=='POST':
        var_staffForm=staffForm(request.POST)
        var_staffAddForm=staffAddForm(request.POST)
        if var_staffForm.is_valid() and var_staffAddForm.is_valid():
            staffprimary=var_staffForm.save()
            staffprimary.set_password(staffprimary.password)
            staffprimary.save()
            staffAdd=var_staffAddForm.save(commit=False)
            staffAdd.staff=staffprimary
            staffAdd.save()
            registered=True
    else:
        var_staffForm=staffForm()
        var_staffAddForm=staffAddForm()
    return render(request,'accounts/registerStaff.html',{'var_staffForm':var_staffForm,'var_staffAddForm':var_staffAddForm,'registered':registered})
    
def userLogin(request):
    invalidlogin=False
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active')
        else:
            invalidlogin=True
            return redirect('/accounts/login/')
    else:
        return render(request,'accounts/login.html',{'invalidlogin':invalidlogin})

@login_required
def dashboard(request):
    try:
        current=Customer.objects.get(customer=request.user)
    except Customer.DoesNotExist:
        current=Staff.objects.get(staff=request.user)
    if current.is_customer:
        return redirect('/customerDash/')
    else:
        return redirect('/staffDash/')
    return render(request,'accounts/dashboard.html')

    

def customerDash(request):
    return redirect('/product/')

def staffDash(request):
    return redirect('/repo/')
