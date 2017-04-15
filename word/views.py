from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Word

# Create your views here.
def leave(request):
  if request.method == 'POST':
    try:
      content = request.POST['content']
      if content == '':
        return HttpResponse(status=401,content='你没有输入任何内容！')
      else:
        try:
          user = request.session['us']
          word = Word(user=user['username'],content=content)
          word.save()
          return HttpResponseRedirect('/index.html')
        except Exception as err:
          print('err',err)
          return HttpResponse(status=401,content='登陆后才能留言')
    except:
      return HttpResponse(status=401,content='你没有输入任何内容！')
  else:
    return HttpResponse(status=401,content='请检查请求method')

def word(request):
  words = Word.objects.all()
  user = request.session.get('us',False)
  return render(request,'word.html',{'user':user,'words':words,'page':0})
