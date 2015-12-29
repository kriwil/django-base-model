from django.contrib import admin


class BaseModelAdmin(admin.ModelAdmin):

    exclude = (
        'created_time',
        'modified_time',
        'is_removed',
        'removed_time',
    )
