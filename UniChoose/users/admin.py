from django.contrib import admin

from users.models import (Account, AccountDepartmentRelations, Preference,
                          Subject)

admin.site.register(Account)
admin.site.register(Subject)
admin.site.register(Preference)
admin.site.register(AccountDepartmentRelations)
