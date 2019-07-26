from django.shortcuts import render, get_object_or_404, redirect # 함수사용
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogPost

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def home(request):
    blogs = Blog.objects
    #블로그 모든 글들을 대상으로
    blog_list=Blog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list,3)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아냄)
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다.
    posts = paginator.get_page(page)

    return render(request,'blog/home.html', {'blogs':blogs,'posts':posts})

def detail(request, pk):
    blog_detail =get_object_or_404(Blog, pk = pk)
    return render(request, 'blog/detail.html', {'blog':blog_detail})

def new(request):
    return render(request, 'blog/new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def blogpost(request):
    # 새로운 데이터 새로운 블로그 글을 저장하는 역할 REQUEST== POST
    if request.method =='POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)# 아직 저장 x timezone 후에 save() 저장
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    # 글쓰기 페이지를 띄어주는 역할  == GET (REQUEST) !== POST           
    else:
        # 단순히 입력받을 수 있는 form을 띄워주라
        form = BlogPost()
        return render(request, 'blog/new.html', {'form':form})


def update(request, pk):
    # 어떤 블로그를 수정할지 블로그 객체를 갖고 오기
    blog_detail = get_object_or_404(Blog, pk = pk)
    # 해당하는 블로그 객체 pk 에 맞는 입력공간
    form = BlogPost(request.POST, instance=blog_detail) # 두번째 인자 instance => pk 번째에 해당하는 객체를 입력하는 공간
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'blog/new.html', {'form': form})

def delete(request, pk):
    blog_detail = get_object_or_404(Blog, pk = pk)
    blog_detail.delete()
    return redirect('home')

        