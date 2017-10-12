from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomModelAdmin(admin.ModelAdmin):
	"""Define admin model for custom User model with no email field."""

	fieldsets = (
		(None, {'fields': ('username','email','phone_no', 'password')}),
		(('Personal info'), {'fields': ('first_name', 'last_name', 'total')}),
		(('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
									   'groups', 'user_permissions')}),
		(('Important dates'), {'fields': ('last_login', 'date_joined')}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'password1', 'password2'),
		}),
	)
	list_display = ('email', 'first_name', 'last_name', 'is_staff')
	search_fields = ('email', 'first_name', 'last_name')
	ordering = ('email',)
	readonly_fields=('total', 'password')

admin.site.register(User, CustomModelAdmin)