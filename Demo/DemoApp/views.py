from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date, timedelta
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
def Dashboard(request):
        if request.method == 'GET':
            current_date=date.today()
            print(current_date)
            event_list = Events.objects.filter(start_date__gte= current_date)
            categories_list = Categories.objects.all() 
            
            # pagination
            
            page = request.GET.get('page', 1)
            paginator = Paginator(event_list, 2)
            try:
                event_page = paginator.page(page)
            except PageNotAnInteger:
                event_page = paginator.page(1)
            except EmptyPage:
                event_page = paginator.page(paginator.num_pages)
            print(event_page)
            context = {
                'event_list' : event_list,
                'categories_list' : categories_list,
                'event_page':event_page,
                }
            return render(request, 'Home_page.html',context=context)
def Logout(request):
    logout(request)
    return redirect('DemoApp:login')
        
        
        
        
        
        
        
        
        
        
        
        