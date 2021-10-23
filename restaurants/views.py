from django.shortcuts import render
from restaurants.models import Restaurant, Food, Comment
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone


def comment(request, id):
    if id:
        r = Restaurant.objects.get(id=id)
    else:
        return HttpResponseRedirect("/restaurants_list/")
    if request.POST:
        visitor = request.POST['visitor']
        content = request.POST['content']
        email = request.POST['email']
        date_time = timezone.localtime(timezone.now()) # 擷取現在時間
        Comment.objects.create(visitor=visitor, email=email, content=content, date_time=date_time, restaurant=r)
    return render(request,'comments.html', locals())

def menu3(request, id):
    if id:
        restaurant = Restaurant.objects.get(id=id)
        return render(request,'menu3.html', locals())
    else:
        return HttpResponseRedirect("/restaurants_list/")

def welcome(request):
    if 'user_name' in request.GET and request.GET['user_name'] != '':
        return HttpResponse('Welcome!~' + request.GET['user_name'])
    else:
        return render(request,'welcome.html', locals())

def list_restaurants(request):
    restaurants = Restaurant.objects.all()
    return render(request,'restaurants_list.html', locals())