# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
# from django import template
from django.template.loader import get_template


def here(request):
    return HttpResponse('媽, 我在這裡')

def math(request,a,b):
    a = int(a)
    b = int(b)
    s = a + b
    d = a - b
    p = a * b
    q = a / b
    t = get_template('math.html')
    return HttpResponse(t.render({'s': s, 'd': d, 'p': p, 'q': q}))

def menu1(request):
    food1 = {'name': '番茄炒蛋', 'price': 60, 'comment': '好吃', 'is_spicy': False}
    food2 = {'name': '蒜泥白肉', 'price': 100, 'comment': '人氣推薦', 'is_spicy': True}
    foods = [food1, food2]
    return render(request, 'menu1.html', locals()) 