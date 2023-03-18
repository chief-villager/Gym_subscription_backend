from django.contrib import admin
from subscription_app .models import Plan,UserPlan

# Register your models here.
admin.site.register(Plan)
admin.site.register(UserPlan)

