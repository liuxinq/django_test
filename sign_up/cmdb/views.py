from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models

# Create your views here.

#user_list = [
#    {"user": "jack", "pwd": "abc"},
#    {"user": "tom", "pwd": "ABC"},
#]

def index(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        models.UserInfo.objects.create(username=username, password=password)
        #temp = {"user": username, "pwd": password}
        #user_list.append(temp)
    user_list = models.UserInfo.objects.all()
    return render(request, "index.html", {"data": user_list})

def hello(request):
    return HttpResponse(u"Hello Django!")
