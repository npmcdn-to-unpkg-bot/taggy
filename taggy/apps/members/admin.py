from django.contrib import admin

# Register your models here.
from taggy.apps.members.models import MemberRole


class MemberRoleAdmin(admin.ModelAdmin):
    pass

admin.site.register(MemberRole, MemberRoleAdmin)
