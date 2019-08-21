from django.shortcuts import render

def index(request):
  return render(request, 'pages/index.html')

def about(request):
  return render(request, 'pages/about.html')

def sell(request):
  return render(request, 'pages/sell.html')