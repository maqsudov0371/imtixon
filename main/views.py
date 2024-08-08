from django.shortcuts import render, get_object_or_404
from .models import *

def home(request):
    posts = Post.objects.order_by('-id')
    users = User.objects.all()
    categorys = Category.objects.all()

    context = {
        'posts': posts,
        'users': users,
        'categorys': categorys      
    }

    return render(request, 'index.html', context)

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category__id=category_id)

    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'category.html', context)


def last_post(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        comment = request.POST.get('comment')
        comment = Comment.objects.create(post=post,  content=comment)
        if request.user.is_authenticated:
            comment.author = request.user
        else:
            comment.first_name = first_name    
            comment.last_name = last_name    
        comment.save()


    if not request.session.get('post'):
        request.session['post'] = []
        request.session['post'].append(post_id)
        post.views += 1
        
    post.save()
    if post.id not in request.session['post']:
        post.views += 1
        request.session['post'].append(post_id)
        request.session.save()
    
    post.save()

    context = {
        'post': post,
    }
    return render(request, 'post.html', context)