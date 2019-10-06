from django.contrib import admin
from .models.globals import Images, BlogPost, MailsSendings, TaskSendidng
from django.utils.html import format_html

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):

    # save_on_top = True
    list_display = ['image','title', 'description', 'alt',]
    # list_editable = ['moderation']
    # readonly_fields = ['obj_name', ]
    # list_filter = ['moderation', 'watched']
    # search_fields = ('name_person', 'email', 'comment_body',)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):

    save_on_top = True
    list_display = ['id', 'show_image', 'main_image', 'title', 'short_description', 'get_short_body', 'availavled',]
    readonly_fields = ['show_image', ]

    def show_image(self, obj):
        return format_html('<a href="{0}" target="_blank"><img src="{0}" width="150px" /></a>'.format(obj.main_image.image.url))

    def get_short_body(self, obj):
        return obj.body[:800] + '  ......'

    show_image.short_description = 'Главное изображение'
    get_short_body.short_description = 'Тело поста'

@admin.register(TaskSendidng)
class MailsSendingsAdmin(admin.ModelAdmin):
    # save_on_top = True
    list_display = ['mail_email','mail_subject', 'mail_body', 'is_complite','date_send','date_created']

@admin.register(MailsSendings)
class MailsSendingsAdmin(admin.ModelAdmin):

    # save_on_top = True
    list_display = ['email','date_last_sending', 'date_created']