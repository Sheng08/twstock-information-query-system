# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView
from numpy import split
from StockSearch.forms import HomeForm
from StockSearch.models import Stock_Information
import matplotlib.pyplot as plt
import twstock
import time
import random, json
from django.views.decorators.csrf import csrf_exempt
from django import forms

# @csrf_exempt
def stock(request):
    if request.method=="GET":    
        
        return render(request,'stock.html',locals())

    else:
        # print(request.body)  # 原始的请求体数据
        # print ("AA", request.POST.get('open_stock_code'))
        # print ("AA", request.POST.get('date'))
        # print ("AA", request.POST.get('stock_name'))
        if request.POST.get('stock_name'):
            
            try:
                text = request.POST.get('stock_name')
                text = int(text)
                text = str(text)
            except:
                for i in twstock.codes:
                    if twstock.codes[i].name==text:
                        text = str(i)
                        break
            try:
                stock1 = twstock.realtime.get(text)
                # print(stock1)
                # print(request.POST.get('open_stock_code'))
                # print(request.POST.get('month'))
                real_search_time = stock1['info']['time']
                code = stock1['info']['code']
                name = stock1['info']['name']
                fullname = stock1['info']['fullname']
                best_bid_price = [i.split('.')[0] for i in stock1['realtime']['best_bid_price']]
                best_bid_volume = [i.split('.')[0] for i in stock1['realtime']['best_bid_volume']]
                best_ask_price = [i.split('.')[0] for i in stock1['realtime']['best_ask_price']]
                best_ask_volume = [i.split('.')[0] for i in stock1['realtime']['best_ask_volume']]
                open = stock1['realtime']['open'].split('.')[0]
                high = stock1['realtime']['high'].split('.')[0]
                low = stock1['realtime']['low'].split('.')[0]
                # print(best_bid_price)
                # print(stock1)
                # f = 123
                # payload='{"fuck":{0}}'.format(123)
                # print(payload)
                # print(json.dumps(best_ask_volume))
                payload = '"real_search_time":"{}", "code":"{}", "name":"{}", "fullname":"{}", "best_bid_price":{}, "best_bid_volume":{}, "best_ask_price":{}, "best_ask_volume":{}, "open":"{}", "high":"{}", "low":"{}"'.format(real_search_time, code, name, fullname,json.dumps(best_bid_price) ,json.dumps(best_bid_volume) ,json.dumps(best_ask_price) ,json.dumps(best_ask_volume) , open, high, low)
                payload='{'+payload+'}'
                # print(payload)
                payload = json.loads(payload)
                print(payload)
                return HttpResponse(json.dumps(payload),content_type='application/json' )
            except KeyError as e:
                print(e)
                return HttpResponse(json.dumps({"error":"stockInfoError"}),content_type='application/json' )
            except Exception as e:
                print(e)
                return HttpResponse(json.dumps({"error":"UnkownError"}),content_type='application/json' )

        # 如何一次判斷是否成功拿到form 不用多個判斷 有按鈕動作??
        if  request.POST.get('open_stock_code') and request.POST.get('year'):
                # print(request.POST.get('open_stock_code'))
                # print(request.POST.get('year'))

                open_stock_code = str(request.POST.get('open_stock_code'))
                year = request.POST.get('year')

                year_day=[]
                year_open=[]
                year_high=[]
                year_low=[]
                year_close=[]
                year_set = Stock_Information.objects.filter(stock_code = open_stock_code, stock_year = year)
                for i in year_set:
                    print('year_set:', i.stock_code, i.stock_year, i.stock_month, i.stock_day, i.stock_open, i.stock_high, i.stock_low, i.stock_close)
                    year_day.append(str(i.stock_year)+'-'+str(i.stock_month)+'-'+str(i.stock_day))
                    year_open.append(str(i.stock_open))
                    year_high.append(str(i.stock_high))
                    year_low.append(str(i.stock_low))
                    year_close.append(str(i.stock_close))
                # print(year_day)
                # best_ask_volume = year_day
                # low = 'sdasdsa'
                # print(low)
                # return render(request,'stock.html',locals())
                payload = '"day":{}, "open":{}, "high":{}, "low":{}, "close":{}'.format(json.dumps(year_day) ,json.dumps(year_open),json.dumps(year_high),json.dumps(year_low),json.dumps(year_close))
                payload='{'+payload+'}'
                # print(payload)
                payload = json.loads(payload)
                # print(payload)
                return HttpResponse(json.dumps(payload),content_type='application/json' )

        elif  request.POST.get('open_stock_code') and request.POST.get('month'):
                # print(request.POST.get('open_stock_code'))
                # print(request.POST.get('month'))

                open_stock_code = str(request.POST.get('open_stock_code'))
                date = request.POST.get('month')
                # print()
                year = date.split('-')[0]
                month = date.split('-')[1] #能用str to datetime

                month_day=[]
                month_open=[]
                month_high=[]
                month_low=[]
                month_close=[]

                month_set = Stock_Information.objects.filter(stock_code = open_stock_code, stock_year = year, stock_month = month)
                # print(month_set)
                for i in month_set:
                    print('month_set:', i.stock_code, i.stock_year, i.stock_month, i.stock_day, i.stock_open)
                    month_day.append(str(i.stock_year)+'-'+str(i.stock_month)+'-'+str(i.stock_day))
                    month_open.append(str(i.stock_open))
                    month_high.append(str(i.stock_high))
                    month_low.append(str(i.stock_low))
                    month_close.append(str(i.stock_close))
                payload = '"day":{}, "open":{}, "high":{}, "low":{}, "close":{}'.format(json.dumps(month_day) ,json.dumps(month_open),json.dumps(month_high),json.dumps(month_low),json.dumps(month_close))
                payload='{'+payload+'}'
                # print(payload)
                payload = json.loads(payload)
                return HttpResponse(json.dumps(payload),content_type='application/json' )

        # if request.POST.get('open_type'):

        #     # open_stock_type = ['6180(橘子)','2317(鴻海)','3008(大立光)','2330(台積電)','2886(兆豐金)','2002(中鋼)','3260(威剛)','2603(長榮)','2377(微星)','2609(陽明)']
        #     open_stock_type = ['6180','2317','3008','2330','2886','2002','3260','2603','2377','2609']
        #     if request.POST.get('open_type')=='year':
        #         open_year = ['2020','2021']
        #         open_type_select = "年開盤"
        #     else:
        #         open_year = ['2020','2021']
        #         open_month = list([i for i in range(1,13)])
        #         open_type_select = "月開盤"
    
        # if  request.POST.get('open_stock_year2') and request.POST.get('open_stock_month') and request.POST.get('open_stock_code'):

        #         year_day=[]
        #         year_open=[]
        #         set1 = Stock_Information.objects.filter(stock_code = str(request.POST.get('open_stock_code')), stock_year = str(request.POST.get('open_stock_year2')), stock_month = str(request.POST.get('open_stock_month')))
        #         print(set1)
        #         for i in set1:
        #             print('set1:',i.stock_code,i.stock_year,i.stock_month,i.stock_day,i.stock_open)
        #             year_day.append(str(i.stock_year)+'-'+str(i.stock_month)+'-'+str(i.stock_day))
        #             year_open.append(str(i.stock_open))

        #         # plt.style.use("ggplot")

        #         # plt.figure(figsize=(250,200))
        #         # plt.xticks(rotation=45,fontsize=10)

        #         # plt.plot(year_day,year_open,'s-',color = 'r')

        #         # plt.xlabel("time", fontsize='20')
        #         # plt.ylabel("price", fontsize='20')
        #         # plt.title(str(i.stock_year)+"年開盤走勢圖", fontproperties="SimSun", fontsize='30') 

        #         # plt.legend(loc = "best", fontsize=20)
                
        # elif request.POST.get('open_stock_year1') and request.POST.get('open_stock_code'):

        #         month_day=[]
        #         month_open=[]
        #         set2 = Stock_Information.objects.filter(stock_code = str(request.POST.get('open_stock_code')), stock_year = str(request.POST.get('open_stock_year1')))
        #         for i in set2:
        #             print('set2:',i.stock_code,i.stock_year,i.stock_month,i.stock_day,i.stock_open)
        #             month_day.append(str(i.stock_year)+'-'+str(i.stock_month)+'-'+str(i.stock_day))
        #             month_open.append(str(i.stock_open))
                
        #         plt.style.use("ggplot")

        #         plt.figure(figsize=(250,200))
        #         plt.xticks(rotation=45,fontsize=10)

        #         plt.plot(month_day, month_open,'s-',color = 'r')

        #         plt.xlabel("time", fontsize='20')
        #         plt.ylabel("price", fontsize='20')
        #         plt.title(str(i.stock_year)+"年"+str(i.stock_month)+"月開盤走勢圖", fontproperties="SimSun", fontsize='30') 

        #         plt.legend(loc = "best", fontsize=20)
        #         plt.show()
                
        # return render(request,'stock.html',locals())

def stock2(request):
    if request.method=="GET":    
        
        return render(request,'stock_old.html',locals())

    else:

        if request.POST.get('stock_name'):
            
            try:
                text = request.POST.get('stock_name')
                text = int(text)
                text = str(text)
            except:
                for i in twstock.codes:
                    if twstock.codes[i].name==text:
                        text = str(i)
                        break
            stock1 = twstock.realtime.get(text)
            real_search_time = stock1['info']['time']
            code = stock1['info']['code']
            name = stock1['info']['name']
            fullname = stock1['info']['fullname']
            best_bid_price = stock1['realtime']['best_bid_price']
            best_bid_volume = stock1['realtime']['best_bid_volume']
            best_ask_price = stock1['realtime']['best_ask_price']
            best_ask_volume = stock1['realtime']['best_ask_volume']
            open = stock1['realtime']['open']
            high = stock1['realtime']['high']
            low = stock1['realtime']['low']
            # print(stock1)
            
        if request.POST.get('open_type'):

            # open_stock_type = ['6180(橘子)','2317(鴻海)','3008(大立光)','2330(台積電)','2886(兆豐金)','2002(中鋼)','3260(威剛)','2603(長榮)','2377(微星)','2609(陽明)']
            open_stock_type = ['6180','2317','3008','2330','2886','2002','3260','2603','2377','2609']
            if request.POST.get('open_type')=='year':
                open_year = ['2020','2021']
                open_type_select = "年開盤"
            else:
                open_year = ['2020','2021']
                open_month = list([i for i in range(1,13)])
                open_type_select = "月開盤"
    
        if  request.POST.get('open_stock_year2') and request.POST.get('open_stock_month') and request.POST.get('open_stock_code'):

                year_day=[]
                year_open=[]
                set1 = Stock_Information.objects.filter(stock_code = str(request.POST.get('open_stock_code')), stock_year = str(request.POST.get('open_stock_year2')), stock_month = str(request.POST.get('open_stock_month')))
                print(set1)
                for i in set1:
                    print('set1:',i.stock_code,i.stock_year,i.stock_month,i.stock_day,i.stock_open)
                    year_day.append(str(i.stock_year)+'-'+str(i.stock_month)+'-'+str(i.stock_day))
                    year_open.append(str(i.stock_open))

                # plt.style.use("ggplot")

                # plt.figure(figsize=(250,200))
                # plt.xticks(rotation=45,fontsize=10)

                # plt.plot(year_day,year_open,'s-',color = 'r')

                # plt.xlabel("time", fontsize='20')
                # plt.ylabel("price", fontsize='20')
                # plt.title(str(i.stock_year)+"年開盤走勢圖", fontproperties="SimSun", fontsize='30') 

                # plt.legend(loc = "best", fontsize=20)
                
        elif request.POST.get('open_stock_year1') and request.POST.get('open_stock_code'):

                month_day=[]
                month_open=[]
                set2 = Stock_Information.objects.filter(stock_code = str(request.POST.get('open_stock_code')), stock_year = str(request.POST.get('open_stock_year1')))
                for i in set2:
                    print('set2:',i.stock_code,i.stock_year,i.stock_month,i.stock_day,i.stock_open)
                    month_day.append(str(i.stock_year)+'-'+str(i.stock_month)+'-'+str(i.stock_day))
                    month_open.append(str(i.stock_open))
                
                plt.style.use("ggplot")

                plt.figure(figsize=(250,200))
                plt.xticks(rotation=45,fontsize=10)

                plt.plot(month_day, month_open,'s-',color = 'r')

                plt.xlabel("time", fontsize='20')
                plt.ylabel("price", fontsize='20')
                plt.title(str(i.stock_year)+"年"+str(i.stock_month)+"月開盤走勢圖", fontproperties="SimSun", fontsize='30') 

                plt.legend(loc = "best", fontsize=20)
                plt.show()
                
        return render(request,'stock_old.html',locals())

# Create your views here.
class HomeView(TemplateView):

    template_name = 'stock.html'

    def get(self,request):
        form = HomeForm()
        # form1 = HomeForm()
        return render(request,self.template_name,{'form':form})
    
    def post(self,request):
        form = HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            form = HomeForm()
            form1 = HomeForm()
            # return redirect('stock:stock')

        try:
            text = int(text)
            stock1 = twstock.realtime.get(str(text))
        except:
            for i in twstock.codes:
                if twstock.codes[i].name==text:
                    text = str(i)
                    break
            stock1 = twstock.realtime.get(text)
        
        #及時查詢
        real_search_time = stock1['info']['time']
        code = stock1['info']['code']
        name = stock1['info']['name']
        fullname = stock1['info']['fullname']
        best_bid_price = stock1['realtime']['best_bid_price']
        best_bid_volume = stock1['realtime']['best_bid_volume']
        best_ask_price = stock1['realtime']['best_ask_price']
        best_ask_volume = stock1['realtime']['best_ask_volume']
        open = str(round(int(stock1['realtime']['open'])))
        # print(open)
        high = stock1['realtime']['high']
        low = stock1['realtime']['low']

        return render(request,self.template_name,locals())

        #資料庫存取
        # year = time.localtime().tm_year
        # month =time.localtime().tm_mon

        # beg_year =  year-1
        # beg_month = month

        # beg_year1 = beg_year
        # beg_month1 = beg_month

        # select_codes = ['6180','2317','3008','2330','2886','2002','3260','2603','2377','2609']

        # cnt = 2
        # for select in select_codes:
        #     while(beg_year1<year or beg_month1<month+1):
        #         stock = twstock.Stock(select)
        #         a = stock.fetch(beg_year1,beg_month1)
        #         time.sleep(random.randint(20,30))
        #         b = twstock.realtime.get(select)
        #         print(select, beg_year1, beg_month1)
        #         beg_month1+=1
        #         if a:
        #             print(a)
        #             for j in a:
        #                 date = str(j.date).split(" ")[0]
        #                 date = date.split("-")
        #                 Stock_Information.objects.create(stock_year = date[0], stock_month=date[1], stock_day=date[2] ,stock_code=select, stock_name = b['info']['name'], stock_capacity = j.capacity, stock_turnover = j.turnover, stock_open = j.open, stock_high = j.high, stock_low = j.low, stock_close = j.close,stock_change = j.change, stock_transaction = j.transaction)
        #             if beg_month1>12:
        #                 beg_month1=1
        #                 beg_year1+=1
        #             time.sleep(random.randint(20,30))
        #     #當一檔股票都讀取完之後
        #     beg_year1 = beg_year
        #     beg_month1 = beg_month
        #     cnt+=1
        #     if cnt>2:
        #         time.sleep(60)
        #         cnt=0

        # Stock_Information.objects.create(stock_year = "2020", stock_month="5", stock_day="1" ,stock_code="2330", stock_name = "台積電", stock_capacity = "72252861", stock_turnover = "21341931218", stock_open = "294.5", stock_high = "296.0", stock_low = "292.5", stock_close = "296.0",stock_change = 0.5, stock_transaction = "16046")
        