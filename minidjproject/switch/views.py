from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import switch_details
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="login")
def addswitch(request):
	if request.method=='POST':
		switch_model=request.POST['switch_model']
		switch_ip=request.POST['switch_ip']
		netmask=request.POST['netmask']
		gateway=request.POST['gateway']
		mac_address=request.POST['mac_address']
		if switch_model !='' and switch_ip !='' and netmask !='' and gateway !='' and mac_address !='':
			if switch_details.objects.filter(switch_ip=switch_ip).exists() != True:
				details=switch_details(switch_model=switch_model,switch_ip=switch_ip,netmask=netmask,gateway=gateway,mac_address=mac_address)
				details.save()
				messages.info(request,'Switch Details Added!')
				return redirect('addswitch')
			else:
				messages.info(request,'Ip Address should be Unique and should not be the existing one!')
				return redirect('addswitch')
		else:
			messages.info(request,'Enter All Switch Details!')
			return redirect('addswitch')
	else:
		return render(request,'addswitch.html')
@login_required(login_url="login")
def main(request):
	list=switch_details.objects.all()
	return render(request,'main.html',{'list':list})
@login_required(login_url="login")
def displaybyIP(request):
     varIP=request.GET['var']
     ip = switch_details.objects.raw('SELECT * FROM switch_switch_details WHERE switch_ip=%s',[varIP])
     return render(request, 'switch_items.html',{'ip': ip})

def login(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			if request.GET.get('next',None):
				return HttpResponseRedirect(request.GET['next'])
			return redirect('main')
			
		else:
			messages.info(request,"Invalid Credentials")
			return redirect('login')
	else:
		return render(request,'login.html')

def register(request):
	if request.method=='POST':
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		username=request.POST['username']
		password1=request.POST['password1']
		password2=request.POST['password2']
		email=request.POST['email']
		if password1==password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,'Username Taken')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.info(request,'Email ID Taken')
				return redirect('register')
			else:
				user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
				user.save();
				messages.info(request,'User Created!')
		else:
			messages.info(request,'Password not matching..')
			return redirect('register')
		return redirect('/')


	else:
		return render(request,'register.html')
@login_required(login_url="login")
def logout(request):
	auth.logout(request)
	return redirect('login')


