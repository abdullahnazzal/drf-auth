from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import Profile
from .forms import PersonCreationForm
# Register your models here.

class PersonAdmin(UserAdmin):
    add_form = PersonCreationForm
    model = Profile
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = ((None,{'fields':('username', 'email', 'first_name', 'last_name', 'password')}),)

# Register your models here.
admin.site.register(Profile, PersonAdmin)