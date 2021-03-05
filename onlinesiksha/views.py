from django.shortcuts import render,get_object_or_404
from .models import Course ,Subject,Teacher
from .forms import ContactForm,SnippetForm
# Create your views here.
def index(request):
	course=Course.objects.all()
	return render(request,"index.html", {'course':course})

def courses(request):
	course=Course.objects.all()
	return render(request,"courses.html", {'course':course})
def coursedetail(request,course_id):
	coredetail = get_object_or_404(Course,pk=course_id)
	return render(request,"coursedetail.html", {'course':coredetail})


def subjects(request):
	subject=Subject.objects.all()
	return render(request,"subjects.html", {'subject':subject})

def about(request):
	teacher=Teacher.objects.all()
	return render(request,"about.html",{'teacher':teacher})

def contact(request):
	
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			Email = form.cleaned_data['Email']

			print(name,Email)



	form = ContactForm()
	return render(request,"contact.html",{'form':form})


def snippet_detail(request):
	
	if request.method == 'POST':
		form = SnippetForm(request.POST)
		if form.is_valid():
			form.save()



	form = SnippetForm()
	return render(request,"contact.html",{'form':form})

 