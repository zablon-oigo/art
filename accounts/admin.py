from django.contrib import admin
from .models import CustomUser,Profile
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin



class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=CustomUser
    list_display=[
        "email",
        "username",
        "is_artist",
        "is_staff",
    ]
    fieldsets=UserAdmin.fieldsets+((None,{"fields":("is_artist",)}),)
    add_fieldsets=UserAdmin.add_fieldsets+((None,{"fields":("is_artist",)}),)

admin.site.register(CustomUser, CustomUserAdmin)



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['user','date_joined']

  

