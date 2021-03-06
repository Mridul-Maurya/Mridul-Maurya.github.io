from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
	if request.method == 'POST':
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request, "signup.html", {'error': 'username is alradey taken' })
			except User.DoesNotExist:
				user=User.objects.create_user(request.POST['username'],password=request.POST['password1'],email=request.POST['email'])
				auth.login(request,user)
				return redirect ('index')
	 
		else:
			return render(request, "signup.html", {'error': 'Password doesn\'t match' })

	return render(request, "signup.html")
def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			auth.login(request,user)
			return redirect('index')
		else:
			return(request,'login.html',{'error':'username or password is incorrect'})
	else:
		return render(request, "login.html")

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('index')
	return render(request, "logout.html")