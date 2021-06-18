import time

import urllib.request
import json
from django.shortcuts import render,redirect
from .models import Report,Profile
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import  CreateUserForm,ProfileForm








def index(request):
    profile=None

    
    

    z=None
    data={}
    ct=0
    mindblowing=0
    avarage=0
    verybad=0
    
    if request.user.is_authenticated:

        profile,_ = Profile.objects.get_or_create(user=request.user)
   

    

    p=Report.objects.filter(intrest="mind blowing")
    for x in p:
        
        mindblowing+=1
    p=Report.objects.filter(intrest="exellent")
    for x in p:
        
        mindblowing+=1    
    p=Report.objects.filter(intrest="avarage")
    for x in p:
        print(x.intrest)
        avarage+=1
    p=Report.objects.filter(intrest="bellow avarage")
    for x in p:
        
        avarage+=1
    p=Report.objects.filter(intrest="very bad")
    for x in p:
        
        verybad+=1
    p=Report.objects.filter(intrest="worst")
    for x in p:
       
        verybad+=1
    now = timezone.now()
    print(now)
    # p=Report.objects.filter(created__date__lte="",created__date__gte="")   
     

    
    post=Report.objects.all()
    for x in post:
        

        ct+=1
    all_post= Report.objects.all()# order by id   
    paginator=Paginator(all_post,3)
    
    page_number=request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # Get the index of the current page
    index = page_obj.number - 1  # edited to something easier without index
    # This value is maximum index of your pages, so the last page - 1
    max_index = len(paginator.page_range)
    # You want a range of 7, so lets calculate where to slice the list
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    # Get our new page range. In the latest versions of Django page_range returns 
    # an iterator. Thus pass it to list, to make our slice possible again.
    page_range = list(paginator.page_range)[start_index:end_index]

    # try:
    #     pst=allpost.page(page)
    #     print(pst)
    # except PageNotAnInteger:
    #     pst=allpost.page(1)

    # except EmptyPage:
    #     pst=allpost.page(allpost.num_pages)






    txt={"ct":ct,"post":page_obj,"page_range":page_range}
   


      
    if request.method == 'POST':
        if request.POST.get('city'):
            
    
            print("its but1")

            city = request.POST['city']

            source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city +
            '&units=metric&appid=a2d4cc68f8cf65ef2daa3a4f68330e3a').read()
            list_of_data = json.loads(source)
    
      
            data = {
            
            "city":city, 
            "country_code":
            str(list_of_data['sys']['country']),
            "coordinate":
            str(list_of_data['coord']['lon']) + ', ' +
            str(list_of_data['coord']['lat']),
            "temp":
            str(list_of_data['main']['temp']) + ' °C',
            "pressure":
            str(list_of_data['main']['pressure']),
            "humidity":
            str(list_of_data['main']['humidity']),
            'main':
            str(list_of_data['weather'][0]['main']),
            'description':
            str(list_of_data['weather'][0]['description']),
            'icon':
            list_of_data['weather'][0]['icon'],
            }

        
            
        elif request.POST.get("choice"):
            

            p=request.POST["choice"]
            
            q=request.POST["review"]
            Report.objects.create(intrest=p,remarks=q,user=request.user,image=profile.avatar,bio=profile.bio)
            return redirect("home")
             
        else:


            data = {} 

            
        
    
    comm={"mindblowing":mindblowing,"avarage":avarage,"verybad":verybad,"profile":profile}    
    z = txt.copy()   # start with x's keys and values
    z.update(data)
    z.update(comm)
        
    
    
    
    
    
    return render(request, "index.html",z)





def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('home')    


@login_required(login_url='login')
def my_profile_view(request):
    


    name=Profile.objects.get(user=request.user)
    cs=Report.objects.filter(user=request.user).update(image=name.avatar)

    profile,_ = Profile.objects.get_or_create(user=request.user)

              



    
   
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    confirm = False

    if form.is_valid():
        form.save()
        confirm = True
        
        return redirect('my')


    context = {
        'profile': profile,
        'form': form,
        'confirm': confirm,
    }
    return render(request, 'main.html', context)
@login_required(login_url='login')   
def indexd(request,stri):
    profile=None
    err=None

    

    profile=Profile.objects.get(hai=stri)
        
   
    context={"profile":profile,"err":err}    

    return render(request,'indexd.html',context)
@login_required(login_url='login')  
def detail(request):

    detail = Report.objects.all()


    context={"detail":detail}
    return render(request,'detail.html',context)    
# Create your views here.