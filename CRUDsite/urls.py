from django.conf.urls import url, include
from CRUDsite import views
from django.views.generic import DetailView, ListView, UpdateView
from .models import *
from .views import *

urlpatterns = [
    url(r'^Home/$',views.home),
    url(r'^institute/$',views.institute),
    url(r'^user/$',views.user),
    url(r'^program/$',views.program),
    url(r'^role/$',views.role),
    url(r'^instutute/delete/$',views.delete),
    url(r'^create/$',views.institute_create),

   # url(r'^institutes/$', views.institute_list, name='institute_list'),
    # List users
    url(r'\^\$', 
        ListView.as_view(
        	queryset=User.objects.all().order_by('name'),
        	template_name='CRUDsite/user_list.html'),
        ),

# User details, ex.: /CRUDsite/user/1/
    url(r'\^user/(?P<pk>\d+)/\$',UserDetail.as_view(),name='user_detail'),

# Create a user, /CRUDsite/user/create/
    url(r'\^user/create/\$',UserCreate.as_view(),name='user_create'),

# Edit user details, ex.: /CRUDsite/user/1/edit/
    url(r'\^user/(?P<pk>\d+)/edit/\$', UpdateView.as_view(
        	model = User,
        	template_name = 'CRUDsite/form.html',
        	form_class = UserForm),
        name='user_edit'),
    ]