from django.shortcuts import render
from .models import Gonderi

def gonderi_liste(request):
    Gonderiler = Gonderi.objects.all()
    return render(request, 'GorkemBlog/gonderi_liste.html', {'Gonderis':Gonderiler})
    