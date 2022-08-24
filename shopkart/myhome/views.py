from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'client/home/dashboard.html')

def productDetailpage(request):
    return render(request, 'client/home/productdetail.html')

def loginpage(request):
    return render(request, 'client/home/login.html')   
    
def aboutpage(request):
    return render(request, 'client/home/about.html')

def categoriespage(request):
    return render(request, 'client/home/categories.html')

def contactpage(request):
    return render(request, 'client/home/contact.html') 

def searchpage(request):
    return render(request, 'client/home/search.html')           


