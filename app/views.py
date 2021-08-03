from django import views
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from django.contrib.auth.decorators import login_required

# Create your views here.

class Login(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(email,password)
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:    
            flag = check_password(password, customer.password)
            if flag:
                print(flag)
                request.session['custome_firstname'] = customer.firstname
                request.session['custome_email'] = customer.email

                return redirect('homepage')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'
        return render(request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')

# @login_required(login_url="/login")
def home(request):
    restaurent = Restaurant.objects.all()
    print(request.session.get('custome_firstname'))
    print("request :- ",request)
    print("request session :-",request.session)
    # name = request.session['email']
    # print(name)
    data = {
        'restaurent':restaurent
    }
    return render(request,'index.html',data)

def menu(request,pk= None):
    menu = Menu.objects.filter(RestaurantName=pk)
    data = {
        'menu':menu,
      
    }
    return render(request,'menu.html',data)

class Signup(View):
    def get(self,request):
        return render(request,'signup.html')
    
    def post(self,request):
        postData = request.POST
        firstname = postData.get('firstname')
        lastname = postData.get('lastname')
        email = postData.get('email')
        password = postData.get('password')
        # print(firstname,lastname,email,password)
        customer = Customer(firstname=firstname,
                            lastname=lastname,
                            email=email,
                            password=password)

        error_message = self.validateCustomer(customer)
        if not error_message:
            customer.password = make_password(customer.password)
            customer.save()
            return redirect('login')
        else:
            data = {
                'error':error_message,
                
            }
            return render(request,'signup.html',data)
        

         # function for validation 
    def validateCustomer(self,customer):
        error_message = None;
        if not customer.firstname:
            error_message = "First Name Required !!"
        elif len(customer.firstname) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not customer.lastname:
            error_message = 'Last Name Required'
        elif len(customer.lastname) < 4:
            error_message = 'Last Name must be 4 char long or more'
        
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
        return error_message
   

class Cart(View):
    def get(self,request,pk = None):

        itemName = Menu.objects.filter(id = pk)
        username =  request.session.get('custome_firstname')
        print(username)
        print(itemName)
        data = {
            "itemName":itemName,
            "username":username
        }
        return render(request,'cart.html',data)

    def post(self,request,pk=None):
        postdata = request.POST
        username = postdata.get('username')
        itemname = postdata.get('itemname')
        price = postdata.get('price')
        phoneno = postdata.get('phoneno')
        address = postdata.get('address')
        restaurant = postdata.get('restaurant')

        print(username,itemname,price,phoneno,address)
        order = Order(username=username,
                            itemname=itemname,
                            price=price,
                            phoneno=phoneno,
                            address=address,
                            restaurant=restaurant,
                            )
        order.save()
        message = "Thankyou for Order Your Oder is Successfully Taken"
        data = {
            "message":message
        }
        return render(request,'cart.html',data)


