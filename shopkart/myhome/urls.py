from django.urls import path,include
from . import views

urlpatterns = [
    path('home/',views.homepage),
    path('detailpage/',views.productDetailpage),
    path('category/',views.categoriespage),
    path('search/',views.searchpage),
    path('about/',views.aboutpage),
    path('contact/',views.contactpage),
    path('login/',views.loginpage),

]