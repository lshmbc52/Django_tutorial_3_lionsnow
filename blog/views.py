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

def post_write(request):
    # post 작성
    # 이전에 했던 question, **choice** 어떤것과 유사한가?
    # form 이용
    if request.method == 'GET':
        form = PostForm()
        context={'form':form}
        return render(request=request, template_name='blog/post_form.html',context=context)
    # elif request.method=='POST':
    #     pass
    else: 
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save() # 내가 저장한 내용이 잘 보이는지 확인하고 싶습니다.
            return redirect('blog:post_detail', post_id=post.id)
            # return redirect('blog:index')