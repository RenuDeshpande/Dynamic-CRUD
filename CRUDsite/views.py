from django.shortcuts import render
from CRUDsite import views
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from .models import *
from .forms import UserForm,InstituteForm,ProgramForm,RoleForm
from django.contrib import messages
# Create your views here.
def home(request):
  return render(request,'CRUDsite/home.html')

def institute(request):
    institutes = Institute.objects.all()
    return render(request, 'CRUDsite/institute-list.html', {'institutes': institutes})

def user(request):
    users = User.objects.all()
    return render(request, 'CRUDsite/institute-list.html', {'institutes': institutes})

def delete(request):
	return render(request,'CRUDsite/delete.html')

def user(request):
  form = UserForm(request.POST or None)
  if(form.is_valid()):
    form.save()
    print('User is created succefully!')
  else:
    print("error")
  return render(request,'CRUDsite/form.html',{'form':form,'entity':'User'})

def program(request):
  form = ProgramForm(request.POST or None)
  if(form.is_valid()):
    form.save()
    print("Suceess!")
  else:
    print("error")
  return render(request,'CRUDsite/form.html',{'form':form,'entity':'Program'})

def institute_create(request):
  form = InstituteForm(request.POST or None)
  if(form.is_valid()):
    form.save()
    print("Suceess!")
  else:
    print("error")
  return render(request,'CRUDsite/form.html',{'form':form,'entity':'Institute'})

def role(request):
  form = RoleForm(request.POST or None)
  if(form.is_valid()):
    form.save()
    print(request,"Suceess!")
  else:
    print("error")
  return render(request,'CRUDsite/form.html',{'form':form,'entity':'Role'})

class UserCreate(CreateView):
  model = User
  template_name = 'CRUDsite/form.html'
  form_class = UserForm

class UserDetail(DetailView):
  model = User
  template_name = 'CRUDsite/user_detail.html'

def delete(request, id):
   institute = Institute.objects.get(pk = id)
   institute.delete()
   return HttpResponse('Institute deleted')

