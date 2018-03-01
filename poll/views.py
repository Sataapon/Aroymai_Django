from django.http import HttpResponse
from django.shortcuts import render, redirect

def home_page(request):
    #if request.method == 'POST':
       #return redirect('/fill')
    return render(request, 'home.html')

def fill_page(request):
    foods = list()
    drinks = list()
    for key in request.POST:
        if key != 'csrfmiddlewaretoken':
            if key[0] == 'f':
                foods.append(request.POST[key])
            else:
                drinks.append(request.POST[key])
    return render(request, 'fill.html', {
        'foods': foods,
        'drinks': drinks,
    })

def add_page(request):
    return HttpResponse("Finish the test!")
        
