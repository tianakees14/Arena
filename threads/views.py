from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from .models import *
# Create your views here.
def index(request):
	return render(request,"index.html",{})

def register(request):
	user = User.objects.create_user(username= request.POST["user_name"],password=request.POST["password"])
	user.save()
	user = authenticate(username= request.POST["user_name"],password=request.POST["password"])
	ob = Profile(user_name = request.POST["user_name"],
				 email_id = request.POST["email"],
				score = 0)
	ob.save()
	login(request,user)
	return render(request,"register.html",{})


def updateDashboard(request):
	try:
		ob = Profile.objects.all().get(user_name = request.user.username)

		form = ImageUploadForm(request.POST, request.FILES)
		if form.is_valid():
			ob.image = form.cleaned_data['image']
		ob.save()
		return redirect('dashboard')
	except:
		return redirect('dashboard')				
		
	
	return redirect('dashboard')				


def dashboard(request):
	ob = Profile.objects.filter(user_name = request.user.username)

	return render(request,"dashboard.html",{'ob':ob})		


def post(request):
	ob = Questions(user_name = request.user.username,
				 question = request.POST["question"],
				 domain= request.POST["domain"])

	ob.save()
	
	return redirect('dashboard')	


def userlogin(request):
	user = authenticate(username= request.POST["username"],password=request.POST["password"])
	login(request,user)



	if user is not None:
		if user.is_active:
			return redirect('dashboard')				


	return HttpResponse("sd")			

def thread(request,id):
	ob = Questions.objects.filter(id = id)
	return render(request,"threads.html",{'ob':ob})


def loginview(request):
	return render(request,"login.html",{})	


def questions(request):
	ob = Questions.objects.all()
	ob2 = Replies.objects.all()

	return render(request,"question.html",{'ob':ob,'ob2':ob2})	

def reply(request):
	ob = Replies(question_id = request.POST["id"],
				reply = request.POST["reply"],
				domain = request.POST["domain"],
				rank = 0,
				votes = 0)	
	ob.save()
	return redirect('questions')