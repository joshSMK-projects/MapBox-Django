from django.shortcuts import render, redirect
from .models import Address
# Create your views here.

def index(request):
    if request.method == 'POST':
        address = Address()
        address.address = request.POST.get('address')
        address.save()
        return redirect('/')

    return render(request, 'index.html', {'Addresses': list(Address.objects.all()), 'access_key': ''})  # Third argument is the context