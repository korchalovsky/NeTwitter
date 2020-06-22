from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField('О себе', blank=True, max_length=500)
    image = models.ImageField('Фото профиля', blank=True, upload_to='NeTwitter/media/profile_photo')
    following = models.ManyToManyField('self',
                                       symmetrical=False,
                                       verbose_name='Мои подписки',
                                       related_name='profile_following')

    @receiver(post_save, sender=User, dispatch_uid="create_profile")
    def update_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def __str__(self):
        return '{}'.format(self.user)


class Article(models.Model):
    author = models.ForeignKey(Profile, verbose_name='Автор', on_delete=models.CASCADE)
    article_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    body = models.CharField('Текст статьи', max_length=1000)

    def __str__(self):
        return 'User: {}, Time {}'.format(self.author, self.article_date)

