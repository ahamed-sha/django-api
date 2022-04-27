from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'descripton', 'completed')

# Register your models here.
admin.site.register(Todo)