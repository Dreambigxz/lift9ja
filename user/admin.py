from django.contrib import admin
from .models import MyUser, PersonalInfomation, UserPreference, ContactUs, TESTIMONIA
from .forms import  UserChangeForm, UserCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
# Register your models here.


class Preference(admin.ModelAdmin):

    search_fields = ['user__email']
    list_display = ('user', 'two_factor_auth')

class Tesify(admin.ModelAdmin):

    search_fields = ['username']
    list_display = ('username', 'active', 'time')

class UserPersonalInfo(admin.ModelAdmin):

    search_fields = ['user__email']
    list_display = ('user', 'date_of_bith', 'user_address', 'state', 'country')

class UserAdmin(BaseUserAdmin):
    # The forms to add and cdate_of_birthhange user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email',  'is_admin', 'is_active', 'date_joined', 'read_message', 'is_blocked')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('full_name', 'otp',
                                      'date_joined', 'mail')}),
        ('Permissions', {'fields': ('is_admin', 'is_active', 'top_admin', 'staff', 'is_blocked', 'gender', 'count_login'
                                    )}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name',
                       'username',
                       'email',
                        'password1',
                       'password2'),
        }),
    )


    search_fields = ('email', 'username', 'full_name')
    ordering = ('email',)
    filter_horizontal = ()

class Contact(admin.ModelAdmin):

    search_fields = ['email']
    list_display = ('email', 'pending', 'date')

admin.site.register(MyUser, UserAdmin)
admin.site.register(PersonalInfomation, UserPersonalInfo)
admin.site.register(UserPreference, Preference)
admin.site.register(TESTIMONIA, Tesify)
admin.site.register(ContactUs, Contact)
admin.site.unregister(Group)
