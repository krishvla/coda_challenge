from django.contrib import admin
from .models import hackers, votes, admincode
# Register your models here.

@admin.register(admincode)
class codeAdmin(admin.ModelAdmin):
    list_display = ['code']
    search_fields = ['code']

@admin.register(hackers)
class hackersAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    search_fields = ['name']

@admin.register(votes)
class votesAdmin(admin.ModelAdmin):
    list_display = ['pk','candidate']
    search_fields = ['candidate']