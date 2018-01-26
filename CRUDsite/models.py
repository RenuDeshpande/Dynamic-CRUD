from django.db import models

# Create your models here.
class Institute(models.Model):
 	name=models.CharField(max_length=50)
 	address=models.TextField(max_length=100)
 	def __unicode__(self):
 		return u"%s" % self.name

class Program(models.Model):
	title=models.CharField(max_length=50)
	description=models.TextField(max_length=100)
	noOfSeats=models.PositiveIntegerField(verbose_name="Number of seats")
	def __unicode__(self):
		return u"%s" % self.title

class User(models.Model):
	name=models.CharField(max_length=50)
	email=models.EmailField(max_length=100)
	phone=models.PositiveIntegerField()
	enrolled=models.ForeignKey(Program,null=True,on_delete=models.CASCADE)
	def __unicode__(self):
		return u"%s" % self.name

class Role(models.Model):
	title=models.CharField(max_length=100)
	def __unicode__(self):
	 return u"%s" % self.title