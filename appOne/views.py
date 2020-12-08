from django.shortcuts import render
from appOne.models import User
# Create your views here.


def index(request):
    return render(request,'appOne/index.html')


def viewers(request):

    user_list = User.objects.order_by('first_name')
    user_dict = {'users' : user_list}
    return render(request,'appOne/viewer.html',context = user_dict)
