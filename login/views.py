from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def signup(request):
  if request.method == 'POST':
    un = request.POST['username']
    pw = request.POST['password']
    try:
      user = User.objects.get(username=un)
      return HttpResponse(status=401)
    except User.DoesNotExist as err:
      user = User(username=un,password=pw)
      user.save()
      request.session['username'] = un
      return HttpResponseRedirect('/index.html')

def login(request):
  f = request.GET.get('f',False)
  if f:
    if f == 'in':
      return render(request,'signin.html')
    elif f == 'up':
      return render(request,'signup.html')
    else:
      return HttpResponse(status=401)
  else:
    return HttpResponse(status=401)

def signin(request):
  if request.method == 'POST':
    un = request.POST['username']
    pw = request.POST['password']
    try:
      user = User.objects.get(username=un)
      if user.password == pw:
        request.session['username'] = un
        return HttpResponseRedirect('/index.html')
      else:
        return HttpResponse(status=403)
    except User.DoesNotExist as err:
      return HttpResponse(status=403)

def logout(request):
  try:
    del request.session['username']
  except KeyError as err:
    pass
  return HttpResponseRedirect('/index.html')
