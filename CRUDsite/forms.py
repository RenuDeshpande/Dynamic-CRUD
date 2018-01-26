from django.forms import ModelForm,Textarea
from django import forms
from .models import *

class InstituteForm(forms.ModelForm):
  class Meta:
    model = Institute
            
    fields = [
             'name',
             'address'
             ]

class UserForm(forms.ModelForm):
  class Meta:
    model = User
            
    fields = [
             'name',
             'email',
             'phone',
             'enrolled'
             ]

class ProgramForm(forms.ModelForm):
  class Meta:
    model = Program
            
    fields = [
             'title',
             'description',
             'noOfSeats'
             ]

class RoleForm(forms.ModelForm):
  class Meta:
    model = Role
            
    fields = [
             'title'
             ]