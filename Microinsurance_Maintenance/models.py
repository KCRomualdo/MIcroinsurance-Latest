from django.db import models
from django import forms
from django.utils import timezone
from datetime import datetime

# Create your models here.

class Branch(models.Model):
	#pass
	#id_number=models.IntegerField(default=1)
	branch_name=models.CharField(default='',max_length=50,verbose_name=' *  Branch name:')
	branch_address=models.TextField(default='',verbose_name=' *  Branch address:')

	def __str__(self):
		return self.branch_name

	class Meta:
		verbose_name_plural="Branches"

class Underwriter(models.Model):
	underwriter_name=models.CharField(max_length=50,verbose_name=' *  Underwriter name:')
	underwriter_ContactNo=models.CharField(max_length=20,default='',verbose_name=' *  Contact number:')
	underwriter_address=models.TextField(default='',verbose_name=' *  Address:')

	def __str__(self):
		return self.underwriter_name

class InsuranceOffer(models.Model):
	#pass
	SKU_name=models.CharField(max_length=50,default='',verbose_name=' *  SKU name:')
	base_price=models.PositiveIntegerField(default=0,verbose_name=' *  Base price of SKU:')
	selling_price=models.PositiveIntegerField(default=0,verbose_name=' *  Selling price of SKU:')
	Valid_days=models.PositiveIntegerField(default=0,verbose_name=' *  Number of valid days:')
	Age_range_from=models.PositiveIntegerField(default=0,verbose_name=' *  Age from:')
	Age_range_to=models.PositiveIntegerField(default=0,verbose_name=' *  Age to:')
	Limit_per_person=models.PositiveIntegerField(default=0,verbose_name=' *  Number of limit for availing this SKU:')
	Underwriter_name=models.ForeignKey(Underwriter,default='',verbose_name=' *  Insurance underwriter:')

	def __str__(self):
		return self.SKU_name

class UserType(models.Model):
	userTypeName=models.CharField(max_length=50,default='',verbose_name=' *  User Type:')

	def __str__(self):
		return self.userTypeName


class User(models.Model):
	firstName=models.CharField(max_length=50,verbose_name=" *  First Name:")
	midName=models.CharField(max_length=50,verbose_name=" Middle Name:",blank='true')
	lastName=models.CharField(max_length=50,verbose_name=" *  Last Name:")
	contactNo=models.CharField(max_length=20,verbose_name=" *  Contact Number:")
	emailAdd=models.CharField(max_length=50,default='',verbose_name=" *  Email Address:")
	user_branch=models.ForeignKey(Branch,default='',verbose_name=' *  Assign branch:')
	user_ptype=models.ForeignKey(UserType,default='',verbose_name=' *  User type:')
	user_uname=models.CharField(max_length=50,verbose_name=" *  Username:",default='')
	user_pword=models.CharField(max_length=50,verbose_name=" *  Password:",default='')

	def __str__(self):
		return "%s %s %s" % (self.firstName,self.midName,self.lastName)

class UserForm(forms.models.ModelForm):
	class Meta:
		model=User
		fields=['user_uname','user_pword']
		widgets={
			'user_uname':forms.fields.TextInput(attrs={
				'placeholder':'username',
				'class':'form-control input-lg',
			}),

			'user_pword':forms.fields.TextInput(attrs={
				'placeholder':'********',
				'class':'form-control input-lg',
			}),
		}

class Promo(models.Model):
	promoName=models.CharField(max_length=50,verbose_name=" *  Promo Name:")
	promoInsurance=models.ForeignKey(InsuranceOffer,default='',verbose_name=' *  Insurance offer:')
	promoPrice=models.PositiveIntegerField(default=0,verbose_name=" *  New price:")
	promoEffectivestartDate=models.DateField(verbose_name=" *  Start Date of the Promo:")
	promoEffectiveendDate=models.DateField(verbose_name=" *  End Date of the Promo:")

	def __str__(self):
		return self.promoName

class Customer(models.Model):
	c_firstName=models.CharField(max_length=50,verbose_name=" *  First Name:")
	c_middleName=models.CharField(max_length=50,verbose_name="   Middle Name:",blank='true')
	c_lastName=models.CharField(max_length=50,verbose_name=" *  Last Name:")
	c_phoneNumber=models.CharField(max_length=20,verbose_name=" *  Contact Number:")

	def __str__(self):
		return "%s %s %s" % (self.c_firstName,self.c_middleName,self.c_lastName)

class CustomerForm(forms.models.ModelForm):
	class Meta:
		model=Customer
		fields=['c_firstName','c_middleName','c_lastName','c_phoneNumber']
		widgets={
			'c_firstName':forms.fields.TextInput(attrs={
				'placeholder':'First name',
				'class':'form-control input-lg',
			}),

			'c_middleName':forms.fields.TextInput(attrs={
				'placeholder':'Middle name',
				'class':'form-control input-lg',
			}),

			'c_lastName':forms.fields.TextInput(attrs={
				'placeholder':'Last name',
				'class':'form-control input-lg',
			}),

			'c_phoneNumber':forms.fields.TextInput(attrs={
				'placeholder':'Any valid contact number',
				'class':'form-control input-lg',
			}),
		}

class Avail(models.Model):
	policyNumber=models.IntegerField(verbose_name=' *  Policy Number:',editable='false')
	customerName=models.ForeignKey(Customer,default='',verbose_name=' *  Customer Name:')
	date_avail=models.DateField(verbose_name=' *  Date availed:',default=datetime.today)
	insurance_avail=models.ForeignKey(InsuranceOffer,verbose_name=' *  Availed Insurance:')

class AvailForm(forms.models.ModelForm):
	class Meta:
		model=Avail
		fields=['policyNumber','date_avail']
		widgets={
			'policyNumber':forms.fields.TextInput(attrs={
				'class':'form-control input-lg',
			}),

			'date_avail':forms.fields.TextInput(attrs={
				'class':'form-control input-lg',
			}),
		}

