from django.shortcuts import render

def home(request):
    return render(request, 'homes/index.html')
