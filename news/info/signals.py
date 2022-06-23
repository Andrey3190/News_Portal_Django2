from django.db.models.signals import m2m_changed
from django.dispatch import receiver  # импортируем нужный декоратор
from django.shortcuts import redirect
from .models import News
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from news.news.tasks import notify_new_post_with_celery

#@receiver(m2m_changed, sender=News.category)
#def notify_users_post(sender, instance, **kwargs):
#    global subscriber
#    sub_text = instance.main_part
#    for category in instance.category.all():
#        for subscriber in category.subscribers.all():
#            print('*********', subscriber.email, '**********')
#            print()
#            print('Адресат:', subscriber.email)
#            html_content = render_to_string(
#                'news/mail.html', {'post': instance, 'text': sub_text[:50], 'category': category.article_text})#

#            msg = EmailMultiAlternatives(
#                subject=f'Здравствуй, {subscriber.username}. Новая статья в вашем разделе!',
#                from_email='andrey-samorukoff@yandex.ru',
#                to=[subscriber.email]
#            )

#            msg.attach_alternative(html_content, 'text/html')


#            print()
#            print(html_content)
#            print()


#        return redirect('/news/')


# Отправка уведомлений подписчикам (по категори поста) при создании нового поста (асинхронный метод с Celery)
@receiver(m2m_changed, sender=News.category)
def notify_new_post(sender, instance, **kwargs):
    notify_new_post_with_celery.apply_async([instance.pk], countdown=10)