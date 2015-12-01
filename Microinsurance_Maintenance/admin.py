from django.contrib import admin
from Microinsurance_Maintenance.models import Branch,Underwriter,InsuranceOffer,UserType,User,Promo
from django.contrib.auth.models import Group

# Register your models here.

admin.site.register(Branch)
admin.site.register(UserType)
admin.site.register(User)
admin.site.unregister(Group)
admin.site.register(Underwriter)
admin.site.register(InsuranceOffer)
admin.site.register(Promo)
