from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.
def blogs(request):
	blog=Blog.objects.all()

	return render(request,"blogs.html", {'blog':blog})

def blogdetail(request,blog_id):
	blodetail = get_object_or_404(Blog,pk=blog_id)
	return render(request,"blogdetail.html", {'blog':blodetail})