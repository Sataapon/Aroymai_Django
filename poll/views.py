from django.http import HttpResponse
from django.shortcuts import render, redirect
from poll.models import Menu, User

def home_page(request):
    return render(request, 'home.html')

def fill_page(request):
    foods = {};
    drinks = {};
    for key in request.POST:
        if key != 'csrfmiddlewaretoken':
            if key[0] == 'F':
                foods[key] = request.POST[key]
            else:
                drinks[key] = request.POST[key]
    return render(request, 'fill.html', {
        'foods': foods,
        'drinks': drinks,
    })

def confirm_page(request):
    return render(request, 'confirm.html')

def add_page(request):
    """
    for key in request.POST:
        if key != 'csrfmiddlewaretoken':
            type_key = key.split("_")
            menu = Menu.objects.get(name = type_key[0])
            if type_key[1] == "Score":
                menu.vote(int(request.POST[key]))
                menu.save()
            elif type_key[1] == "Comment":
                Comment.objects.create(menu = menu, text = request.POST[key])
    return redirect('/view')
    """
    return HttpResponse("AddPage")

def review_page(request):
    return render(request, 'review.html')
