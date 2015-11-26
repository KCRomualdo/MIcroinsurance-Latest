from django.contrib import admin
from branch.models import Branch
from django.contrib.auth.models import Group

# Register your models here.

admin.site.register(Branch)
admin.site.unregister(Group)
