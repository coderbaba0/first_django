from django.shortcuts import get_object_or_404, render
from .models import BlogPost  # Import the BlogPost model

def home(request):
    # Fetch all blog posts from the database
    blog_posts = BlogPost.objects.all()

    # Pass the blog posts to the template
    return render(request, 'myapp/home.html', {'blog_posts': blog_posts})

def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'myapp/post_detail.html', {'post': post})