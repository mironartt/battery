from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Images(models.Model):

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    image = models.ImageField(verbose_name='Изображение')
    title = models.CharField(max_length=500, verbose_name='Заголовок', null=True, blank=True)
    description = models.CharField(max_length=500, verbose_name='Описание', null=True, blank=True)
    alt = models.CharField(max_length=80, verbose_name='Краткое описание (alt)', null=True, blank=True)

    def __str__(self):
        return '(id: {0}) {1} {2}'.format(self.id, self.title if self.title else '', '(%s)' % self.alt if self.alt else '')


class MailsSendings(models.Model):

    class Meta:
        verbose_name = 'Email подписанный на рассылку уведомлений'
        verbose_name_plural = 'Emails подписанные на рассылку уведомлений'

    email = models.EmailField(verbose_name='Email')
    date_last_sending = models.DateTimeField(null=True, verbose_name='Дата последнего отпраления')

    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')


class BlogPost(models.Model):

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    main_image = models.ForeignKey(Images, on_delete=models.CASCADE, verbose_name='Главное изображение поста')
    title = models.CharField(max_length=500, verbose_name='Заголовок')
    short_description = models.CharField(max_length=500, verbose_name='Краткое описание', null=True)
    body = RichTextUploadingField(verbose_name='Текс на главной странице')
    availavled = models.BooleanField(default=True, verbose_name='Отображать на сайте')

    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    need_sending = models.BooleanField(default=True, verbose_name='Необходимо ли разослать подписчикам')
    send_already = models.BooleanField(default=False, verbose_name='Расласть сразу (или по расписанию)')


    def __str__(self):
        return self.title


class TaskSendidng(models.Model):

    class Meta:
        verbose_name = 'Задача на рассылку'
        verbose_name_plural = 'Задачи на рассылку'

    mail_email = models.ForeignKey(MailsSendings, on_delete=models.DO_NOTHING, verbose_name='Адрес еmail')
    mail_subject = models.CharField(max_length=200, verbose_name='Тема письма')
    mail_body = models.TextField(verbose_name='Тело письма')

    is_complite = models.BooleanField(default=False, verbose_name='Выполнен')

    date_send = models.DateTimeField(verbose_name='Дата отправки', null=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

