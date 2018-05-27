from django.shortcuts import render, redirect
from poll.models import Menu, User, CommentScore

def home_page(request):
    foods = Menu.objects.filter(Type = "Food")
    drinks = Menu.objects.filter(Type = "Drink")
    return render(request, 'home.html', {
        'foods': foods,
        'drinks': drinks
    })

def fill_page(request):
    foods = []
    drinks = []
    for key in request.GET:
        if key != 'csrfmiddlewaretoken':
            if key[0] == 'F':
                foods.append(request.GET[key])
            else:
                drinks.append(request.GET[key])
    model_sort(foods)
    model_sort(drinks)
    return render(request, 'fill.html', {
        'foods': foods,
        'drinks': drinks
    })

def add_page(request):
    if request.POST["User"] == "":
        user = User.objects.create(name="Noname")
    else:
        user = User.objects.create(name = request.POST["User"])
    for key in request.POST:
        if (key != 'csrfmiddlewaretoken' and key != 'User'):
            type_key = key.split("_")
            menu = Menu.objects.get(name = type_key[0])
            if (not CommentScore.objects.filter(menu = menu, user = user).exists()):
                CommentScore.objects.create(menu = menu, user = user)
            commentScore = CommentScore.objects.get(menu = menu, user = user)
            if type_key[1] == "comment":
                commentScore.comment = request.POST[key]
            else:
                commentScore.score = request.POST[key]
            commentScore.save()
    return redirect('/')

def review_page(request):
    foods = []
    drinks = []
    for key in request.GET:
        if key != 'csrfmiddlewaretoken':
            if key[0] == 'F':
                foods.append(request.GET[key])
            else:
                drinks.append(request.GET[key])
    model_sort(foods)
    model_sort(drinks)
    foods_cmscs = []
    drinks_cmscs = []
    for food in foods:
        latest_cmsc_food = Menu.objects.get(name = food).commentscore_set.order_by('-id')[:5]
        foods_cmscs.append(latest_cmsc_food)
    for drink in drinks:
        latest_cmsc_drink = Menu.objects.get(name = drink).commentscore_set.order_by('-id')[:5]
        drinks_cmscs.append(latest_cmsc_drink)

    return render(request, 'review.html', {
        'foods': foods,
        'drinks': drinks,
        'foods_cmscs': foods_cmscs,
        'drinks_cmscs': drinks_cmscs
    })

def about_page(request):
    return render(request, 'about.html')

def model_sort(list):
    for i in range(len(list) - 1, 0, -1):
        for j in range(i):
            if Menu.objects.get(name=list[j]).id > Menu.objects.get(name=list[j + 1]).id:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
