from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import BlogPost

# Create your views here.

def index(request):
	# Return the blog posts in an ascending order
	blog_posts = BlogPost.objects.all()[::-1]
	return render(request, 'blogs/blogposts.html', {'blog_posts': blog_posts, 'active': 0})

def detail(request, blog_id):
	# Return a detail page for the post
	blog = get_object_or_404(BlogPost, pk=blog_id)
	return render(request, 'blogs/post.html', {'blog': blog, 'active': 0})
