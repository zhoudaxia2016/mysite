from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from markdown2 import markdown
from comment.models import Comment
import math

# Create your views here.
# 获取标签或者类别
def filter(request,posts):
  t = request.GET.get('t',False)
  ta = request.GET.get('ta',False)
  if t:
    posts = [post for post in posts if post.family and post.family.name == t ]
  if ta:
    posts =  [post for post in posts if ta in[tag.name for tag in post.tags.all()]]
  page = int(request.GET.get('page',1))
  pages = math.ceil(len(posts)/10)
  posts = posts[(page-1)*10:page*10]
  return [posts,page,pages]
  
#排序
def sort(request,posts):
  s = request.GET.get('s',False)
  if s:
    if s == 'n':
      return sorted(posts,key=lambda p:p.publish_time,reverse=True)
    else:
      return sorted(posts,key=lambda p:p.view,reverse=True)
  else:
    return sorted(posts,key=lambda p:p.publish_time,reverse=True)

def index(request):
  posts = []
  posts.extend(Blog.objects.all())
  posts.extend(Demo.objects.all())
  family = Family.objects.all()
  tags = Tag.objects.all()
  posts = sort(request,posts)
  result = filter(request,posts)
  posts = result[0]
  user = request.session.get('us',False)
  return render(request,'index.html',{'pageNum':result[1],'pages':range(1,result[2]+1),'user':user,'posts':posts,'page':0,'family':family,'tags':tags})


def blog(request):
  posts = Blog.objects.all()
  family = Family.objects.all()
  tags = Tag.objects.all()
  posts = sort(request,posts)
  result = filter(request,posts)
  posts = result[0]
  user = request.session.get('us',False)
  return render(request,'index.html',{'pageNum':result[1],'pages':range(1,result[2]+1),'user':user,'posts':posts,'page':1,'family':family,'tags':tags})

def demo(request):
  posts = Demo.objects.all()
  tags = Tag.objects.all()
  posts = sort(request,posts)
  result = filter(request,posts)
  posts = result[0]
  user = request.session.get('us',False)
  return render(request,'index.html',{'pageNum':result[1],'pages':range(1,result[2]+1),'user':user,'posts':posts,'page':2,'tags':tags})

def about(request):
  user = request.session.get('us',False)
  return render(request,'about.html',{'user':user,'page':3})

def event(request):
  events = Event.objects.all()
  user = request.session.get('us',False)
  return render(request,'event.html',{'user':user,'events':events,'page':3})

def detail(request,id):
  try:
    blog=Blog.objects.get(id=id)
    blog.view += 1
    blog.save()
    blog.content = markdown(blog.content)
    user = request.session.get('us',False)
    comments = Comment.objects.filter(blog=id)
    return render(request,'blog.html',{'comments':comments,'user':user,'blog':blog,'page':1})
  except Blog.DoesNotExist as err:
    return HttpResponse(status=404)
