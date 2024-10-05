from django.http import HttpResponse
from django.shortcuts import render,redirect
from store.models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm,UserupdateFrom,ChangePasswordForm,UserProfileForm
from django.shortcuts import render, get_object_or_404
from .models import Profile
import json
from cart.cart import Cart
from payment.forms import  ShippingForm
from payment.models import  ShippingAddress


# user login function
def user_login(request):
    if request.method=='POST':
        name=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=name,password=password)
        if user is not None:
            login(request,user)
            # get the profile object
            current_user=Profile.objects.get(user__id=request.user.id)
            # get the old_cart object from profile model
            saved_cart=current_user.old_cart
            if saved_cart :
                # convert the saved_cart  string to a dictionary
                converted_cart=json.loads(saved_cart)
                cart=Cart(request)
                for key,value in converted_cart.items():
                    cart.db_add(product=key,quantity=value)
            messages.success(request,'You are now logged in ')
            return redirect('home')
        else :
            messages.success(request,'incorrect username or password')
            return redirect('login') 
    else :    
       return render(request,'login.html',{})


# user logout function
def user_logout(request):
    logout(request)
    messages.success(request,'You have been logged out successfully')
    return redirect('home')


# User Registration function
def user_register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Account was successfully created')
                return redirect('home')
            else:
                messages.error(request, 'Authentication failed. Please try again.')
                return redirect('home')
        else:
            messages.error(request, 'There was an error and the account was not created successfully')
            return render(request, 'register.html', {'form': form})
    else:
        return render(request, 'register.html', {'form': form})


# update the user profile information
def update_user_info(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserupdateFrom(data=request.POST, instance=request.user)
            update = form.save(commit=False)
            update.user = request.user
            update.save()
            messages.success(request,'Your profile has been changed successfully')
        else:
            form = UserupdateFrom(instance=request.user)

        return render(request, 'update_user_details.html', {'form': form})
            
            
# function to change the user paswords
def change_password(request):
    if request.user.is_authenticated:
        current_user=request.user
        form =ChangePasswordForm(current_user,request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your password has been changed successfully')
            login(request,current_user)
            return redirect('home')
        else :
            form=ChangePasswordForm(current_user)
            return render(request,'change_pass.html',{'form':form})   
    else :
        messages.success(request,'You must have logged in to change your password') 
        return redirect('home')    
        

# update or create  the profile informations

def update_profile(request):
    if request.user.is_authenticated:
        # Get Current User Profile
        current_user = Profile.objects.get(user__id=request.user.id)
        # Get or create Current User's Shipping Info
        shipping_user, created = ShippingAddress.objects.get_or_create(user=request.user)
        
        # Get original User Form
        form = UserProfileForm(request.POST or None, instance=current_user)
        # Get User's Shipping Form
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        
        if form.is_valid() and shipping_form.is_valid():
            # Save original form
            form.save()
            # Save shipping form
            shipping_form.save()

            messages.success(request, "Your Info Has Been Updated!")
            return redirect('home')
        return render(request, "update_profile.html", {'form': form, 'shipping_form': shipping_form})
    else:
        messages.error(request, "You Must Be Logged In To Access That Page!")
        return redirect('home')
