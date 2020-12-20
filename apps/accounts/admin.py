from django.contrib import admin

# Register your models here.
from apps.accounts.models import WorkerProfile, Message, WorkerCategory, WorkingArea


@admin.register(WorkerCategory)
class WorkerCategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]
    prepopulated_fields = {'slug':('name',),}

@admin.register(WorkingArea)
class WorkerAreaAdmin(admin.ModelAdmin):
    list_display = ['name',]
    prepopulated_fields = {'slug': ('name',), }

@admin.register(WorkerProfile)
class WorkerProfileAdmin(admin.ModelAdmin):
    list_display = ['user','category','working_time','hourly_rate','extra_service','experience','phone',
                    'views','created']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass

