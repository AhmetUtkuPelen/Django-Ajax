from django.shortcuts import render
from .urls import*
import requests

# Create your views here.

API_KEY = '9018c98f43cc4f5f8a7a42207ae84947'


def index(request):
    country = request.GET.get('country')
    
    category = request.GET.get('category')
    
    if country: 
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
    
    
        articles = data['articles']
    
    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        
        articles = data['articles']
    
    context = {
        'articles':articles
    }
    return render(request,'newsapi/index.html',context)