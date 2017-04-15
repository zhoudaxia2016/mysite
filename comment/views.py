from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect  
from .models import Comment

# Create your views here.
def comment(request):
  if request.method == 'POST':
    try:
      content = request.POST['content']
      if content == '':
        return HttpResponse(status=401,content='你没有输入任何内容！')
      else:
        try:
          user = request.session['us']
          blog = request.POST['blog']
          comment = Comment(blog=blog,user=user['username'],content=content)
          comment.save()
          return HttpResponseRedirect('/detail/%s' %blog)
        except Exception as err:
          return HttpResponse(status=401,content='登陆后才能评论！')
    except:
      return HttpResponse(status=401,content='你没有输入任何内容！')
  else:
    return HttpResponse(status=401,content='请检查请求method')
