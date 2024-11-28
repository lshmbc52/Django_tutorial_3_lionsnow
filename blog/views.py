from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Post
from .forms import CategoryForm, PostForm

# Create your views here.
def index(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    context = {'categories':categories,
               'posts':posts
               }
    return render(request, 'blog/index.html', context)

def category_list(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request, 'blog/category_list.html', context)

def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        # 유효성 검증
        if form.is_valid():
            form.save()
            return redirect('blog:category_list')

        pass
    elif request.method == "GET": # form 입력하는 페이지는 표시
        form = CategoryForm()  
    return render(request, 'blog/category_form.html', context={'form':form})
            
def post_detail(request, post_id):
    # post_id의 post를 보내주기
    post = Post.objects.get(pk=post_id)
    categories = Category.objects.all()
    context = {'post':post,'categories':categories}
    return render(request, 'blog/post_detail.html', context)

def category_post_list(request, category_id):
    # category_id인 카테고리에 속한 포스트들의 리스트를 보여주기
    category = get_object_or_404(Category, id=category_id)
    categories = Category.objects.all()

    posts = Post.objects.filter(category=category)
    context = {'posts':posts, 'category':category, 'categories':categories}
    return render(request, 'blog/index.html', context)