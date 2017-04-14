from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from markdown2 import markdown

# Create your views here.
# 获取标签或者类别
def filter(request,posts):
  t = request.GET.get('t',False)
  ta = request.GET.get('ta',False)
  if t:
    return [post for post in posts if post.family and post.family.name == t ]
  elif ta:
    return [post for post in posts if ta in[tag.name for tag in post.tags.all()]]
  else:
    return posts
  
#排序
def sort(request,posts):
  s = request.GET.get('s',False)
  if s:
    if s == 'n':
      return sorted(posts,key=lambda p:p.publish_time,reverse=True)
    else:
      return sorted(posts,key=lambda p:p.view,reverse=True)
  else:
    return posts

def index(request):
  posts = []
  posts.extend(Demo.objects.all())
  posts.extend(Blog.objects.all())
  family = Family.objects.all()
  tags = Tag.objects.all()
  posts = sort(request,posts)
  posts = filter(request,posts)
  return render(request,'index.html',{'posts':posts,'page':0,'family':family,'tags':tags})


def blog(request):
  posts = Blog.objects.all()
  family = Family.objects.all()
  tags = Tag.objects.all()
  posts = sort(request,posts)
  posts = filter(request,posts)
  return render(request,'index.html',{'posts':posts,'page':1,'family':family,'tags':tags})

def demo(request):
  posts = Demo.objects.all()
  tags = Tag.objects.all()
  posts = sort(request,posts)
  posts = filter(request,posts)
  return render(request,'index.html',{'posts':posts,'page':2,'tags':tags})

def about(request):
  return render(request,'about.html',{'page':3})

def event(request):
  events = Event.objects.all()
  return render(request,'event.html',{'events':events,'page':3})

def detail(request,id):
  try:
    blog=Blog.objects.get(id=id)
    blog.view += 1
    blog.save()
    blog.content = markdown(blog.content)
    return render(request,'blog.html',{'blog':blog,'page':1})
  except Blog.DoesNotExist as err:
    return HttpResponse(status=404)
