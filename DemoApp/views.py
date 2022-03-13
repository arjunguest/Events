from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date
from django.http import JsonResponse
import json
# Forms
from DemoApp.forms import LoginForm
# Models 
from DemoApp.models import Events,Categories


# Create your views here.
def Login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('DemoApp:dashboard')
            else:
                return redirect('DemoApp:login')
    else:
        form= LoginForm()
        return render(request,'pages-login.html',{'form' : form})
def Dashboard(request,id=None):
        if request.method == 'POST' and request.is_ajax():
            if request.POST['action'] == 'date_event_action':
                cat_event = request.POST.get('Date_key')
                date_db = Events.objects.filter(start_date= cat_event)
                if date_db is not None:
                    date_list=[]   
                    for dte in date_db:
                        dt_item={}
                        if dte.paid == True:    
                            dt_item={
                                'pk':dte.pk,
                                'title':dte.title,
                                'description' : dte.description,
                                'location':dte.location,
                                'image':str(dte.image.url),
                                'categories':dte.categories.category,
                                'start_date':dte.start_date,
                                'end_date':dte.end_date,
                                'published':dte.published,
                                'paid':'Ticket activated',
                            }      
                            date_list.append(dt_item)
                        else:
                            dt_item={
                                'pk':dte.pk,
                                'title':dte.title,
                                'description' : dte.description,
                                'location':dte.location,
                                'image':str(dte.image.url),
                                'categories':dte.categories.category,
                                'start_date':dte.start_date,
                                'end_date':dte.end_date,
                                'published':dte.published,
                                'paid':'Ticket not activated',
                            }      
                            date_list.append(dt_item)
                    date_res= date_list
                    
                else:
                    date_res= 'No result found..'
                return  JsonResponse({'date_res':date_res})
                
            if request.POST['action'] == 'search_event_action':
                pick_search=request.POST.get('search_key')
                
                search_db = Events.objects.filter(title__icontains= pick_search) | Events.objects.filter(
                    location__icontains= pick_search)
                if len(search_db) > 0 and  len(pick_search) > 0:
                    data=[]
                    for pos in search_db:
                        items = {
                            'pk':pos.pk,
                            'title':pos.title,
                            'description' : pos.description,
                            'location':pos.location,
                            'image':str(pos.image.url),
                            'categories':pos.categories.category,
                            'start_date':pos.start_date,
                            'end_date':pos.end_date,
                            'published':pos.published,
                            'paid':pos.paid,
                        }
                        data.append(items)
                    res= data
                else:
                    res= 'No result found..'
                return  JsonResponse({'data': res})
            
        else:
            current_date=date.today()
            print(current_date)
            event_list = Events.objects.filter(start_date__gte= current_date)
            categories_list = Categories.objects.all() 
            
            # pagination
            
            page = request.GET.get('page', 1)
            paginator = Paginator(event_list, 10)
            try:
                event_page = paginator.page(page)
            except PageNotAnInteger:
                event_page = paginator.page(1)
            except EmptyPage:
                event_page = paginator.page(paginator.num_pages)
            context = {
                'event_list' : event_list,
                'categories_list' : categories_list,
                'event_page':event_page,
                }
            return render(request, 'Home_page.html',context=context)
def EventDetails(request,pk):
    print('pk',pk)
    event_db=Events.objects.filter(pk=pk)
    print("event_db",event_db)
    context={
        "event_db":event_db,
        }
    return render(request, 'Event.html',context=context)
            
def Logout(request):
    logout(request)
    return redirect('DemoApp:login')
        
        
        
        
        
        
        
        
        
        
        
        