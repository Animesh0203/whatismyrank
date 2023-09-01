from django.contrib import admin
from .models import links
from django.contrib.auth.admin import UserAdmin
from mainapp.models import Account

admin.site.register(links)

class AccountAdmin(UserAdmin):
	list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
	search_fields = ('email', 'username',)
	readonly_fields = ('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Account, AccountAdmin)
