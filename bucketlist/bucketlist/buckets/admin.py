from django.contrib import admin
from . import models


@admin.register(models.Bucket)
class ImageAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = (
        'creator',
        'bucket',
        'created_at',
        'updated_at',
    )


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
        'message',
        'creator',
        'bucket',
        'created_at',
        'updated_at',
    )

