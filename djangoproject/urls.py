"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url
# from restaurants.views import menu3,welcome,list_restaurants,comment
# from restaurants.models import Restaurant, Food, Comment

from StockSearch.views import  HomeView, stock, stock2

# from genre.views import here,math,menu1

#app 1
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('here/', here),
#     re_path(r'(\d{1,2})/math/(\d{1,2})/', math),
#     path('menu/', menu1),
# ]

#app Stock
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('stock/', HomeView.as_view()),
    path('stock/', stock),
    path('stock_old/', stock2),
    url('^stock', stock),
]

#app 2_1
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('menu/', menu),
# ]

#app 2_2
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('menu3/', menu3),
#     re_path(r'menu3/(\d{1,5})', menu3),
#     # path('meta/', meta),
#     path('welcome/', welcome),
#     path('restaurants_list/', list_restaurants),
#     re_path(r'comment/(\d{1,5})', comment),
# ]

# admin.site.register(Comment)

#模型註冊
# class RestaurantAdmin(admin.ModelAdmin):
#     list_display = ('name', 'phone_number', 'address')

# class FoodAdmin(admin.ModelAdmin):
#     list_display = ('name', 'restaurant', 'price')
#     list_filter = ('is_spicy',)

# admin.site.register(Restaurant, RestaurantAdmin)
# admin.site.register(Food, FoodAdmin)

