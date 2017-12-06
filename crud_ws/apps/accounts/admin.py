from django.contrib import admin

from crud_ws.apps.accounts.models import User

admin.site.register(User, admin.ModelAdmin)
