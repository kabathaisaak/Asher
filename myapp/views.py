from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')
def gallery(request):
    return render(request, 'gallery.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request,'contact.html')

def list(request):
    return render(request,'list.html')