from django.http import HttpResponse
from django.shortcuts import render,redirect
from store.models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from .models import Product,Category
from fuzzywuzzy import fuzz  
from django.db.models import Q

# search product
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        all_products = Product.objects.all()
        matching_products = []
        min_match_length = int(len(searched) * 0.3)

        for product in all_products:
            if (searched.lower() in product.name.lower()) and (len(searched) > min_match_length):
                matching_products.append(product)

        if not matching_products:
            messages.success(request, 'OOPs! There is no product.')
            return render(request, 'search.html', {})
        else:
            return render(request, 'search.html', {'searched': matching_products})
    else:    
        return render(request, 'search.html', {})
    
    

def home(request):
    products=Product.objects.all()
    return render(request,'home.html',{'products':products})

# Show the information of the single product 
def product(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'product.html', {'product': product})


def about(request): 
    return render(request,'about.html')




# category 
def category(request,cato):
    cato=cato.replace('-',' ')
    try :
        category=Category.objects.get(name=cato)
        products=Product.objects.filter(category=category)
        return render(request,'category.html',{'products':products,'category':category})
        
    except:
        messages.success(request,'There was an error or the category was not exist')
        return redirect('home')
    
    
 

        