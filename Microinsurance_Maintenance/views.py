from django.shortcuts import render
from Microinsurance_Maintenance.models import UserForm,User,CustomerForm,AvailForm,UserType,Customer
from django import forms
from django.http import HttpResponseRedirect

# Create your views here.

def home_page(request):
	if request.method=="GET":
		form=UserForm
		return render(request,'index.html',{'form':form})
	elif request.method=="POST":
		form=UserForm(request.POST)

		if form.is_valid():
			uname=request.POST.get('user_uname')
			pword=request.POST.get('user_pword')

			list_of_users=User.objects.all()

			usertype1=UserType.objects.get(userTypeName="Manager")

			for user in list_of_users:

				if uname==user.user_uname and pword==user.user_pword and user.user_ptype==usertype1:
					#return HttpResponseRedirect("/transaction/register/")
					return render(request,'sample2.html')

			usertype2=UserType.objects.get(userTypeName="Frontliner")

			for user in list_of_users:

				if uname==user.user_uname and pword==user.user_pword and user.user_ptype==usertype2:
					return HttpResponseRedirect("/transaction/register/")


			usertype3=UserType.objects.get(userTypeName="Underwriter")

			for user in list_of_users:

				if uname==user.user_uname and pword==user.user_pword and user.user_ptype==usertype3:
					#return HttpResponseRedirect("/transaction/register/")
					return render(request,'sample2.html')

		else:
			return render(request,'sample2.html')


def transaction_page(request):
	if request.method=="GET":
		form=CustomerForm
		return render(request,'transaction.html',{'form':form})

	elif request.method=="POST":
		form=CustomerForm(request.POST)

		if form.is_valid():	
			#form.save()
			customerdetails=Customer()
			customerdetails.c_firstName=request.POST.get('c_firstName')
			customerdetails.c_middleName=request.POST.get('c_middleName')
			customerdetails.c_lastName=request.POST.get('c_lastName')
			customerdetails.c_phoneNumber=request.POST.get('c_phoneNumber')
			customerdetails.save()

			return HttpResponseRedirect("/transaction/register/")

def transaction_avail_page(request):
	if request.method=="GET":
		form=AvailForm
		list_of_customer=Customer.objects.all()
		for item in list_of_customer:
			Customerlist=item.c_firstName

		return render(request,'transaction_avail.html',{'form':form,'registered_customer':Customerlist})
	elif request.method=="POST":
		form=UserForm(request.POST)


	


