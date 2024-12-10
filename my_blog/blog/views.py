from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Comment
from .forms import CommentForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm 
# View for user registration
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})

# View for user login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

def home(request):
    posts = BlogPost.objects.all()
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogPostForm()

    return render(request, 'blog/home.html', {'posts': posts, 'form': form})

# BlogPost Detail View with Login Required for Commenting
def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    comments = post.comments.all()
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.name = request.user.username
            comment.save()
    else:
        form = CommentForm()
    
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})

def add_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Rediriger vers la page d'accueil après l'ajout
    else:
        form = BlogPostForm()

    return render(request, 'blog/add_blog_post.html', {'form': form})