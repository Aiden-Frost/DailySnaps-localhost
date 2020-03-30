from django.shortcuts import render,redirect
from django.urls import reverse
#import requests
#from newsapi import NewsApiClient
#from news.models import Headline

# Create your views here.

def home_page(request):
    return render(request,'news/index.html', {})