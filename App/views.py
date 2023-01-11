from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm,ProductForm
from .models import User,Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView
import json

from django.views.generic import UpdateView
from django.urls import reverse_lazy
# Create your views here.




def loginpage(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/home')  
		else:
			return redirect('/login')
	
	return render(request, 'login.html')



@login_required
def home(request):
    plist = Product.objects.filter(status='ACTIVE')
    return render(request,'home.html',{'plist':plist})



def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/login")
	form = NewUserForm()
	return render (request,'register.html',{'form':form})

@login_required
def custom_logout(request):
    logout(request)
    return redirect("/login")

def addproduct(request):
	if request.method == "POST":
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/addproduct")
	form = ProductForm()
	return render (request,'addproduct.html',{'form':form})


def productlist(request):
    f = open('D:/COMPANIES INTERVIEW/INDIA/E-COMMERCE/E-COMMERCE/App/product.json', 'r')
    if f.mode == 'r':
       contents =f.read()
       json_string = json.loads(contents)
    #    print(json_string)
    plist = Product.objects.all()
    # print(plist)
    return render (request,'productlist.html',{'plist':plist,'json_string':json_string})
    
    
def productdelete(request,product_id):
    pdt = Product.objects.get(product_id=product_id)
    pdt.delete()
    return redirect('/productlist')

# class ProductUpdate(UpdateView): 
#     model = Product
#     fields = '__all__'
#     template_name = 'addproduct.html'
#     success_url = reverse_lazy('/productlist')

# def edit(request, product_id):  
#     pdt = Product.objects.get(product_id=product_id)  
#     return render(request,'edit.html', {'pdt':pdt}) 

# def update(request, product_id):  
#     pdt = Product.objects.get(product_id=product_id)  
#     form = ProductForm(request.POST, instance = pdt) 
#     print("hiiii") 
#     if form.is_valid():  
#         form.save()
#         return redirect("/productlist")
    
#     print(form.errors )
#     return render(request, 'edit.html', {'pdt': pdt}) 


class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'addproduct.html'
    success_url = reverse_lazy('productlist')
    
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'addproduct.html'
    success_url = reverse_lazy('productlist')   