# Generated by Django 3.0.7 on 2020-06-21 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NeTwitter', '0008_auto_20200621_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(related_name='profile_following', to='NeTwitter.Profile', verbose_name='Мои подписки'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='NeTwitter/media/profile_photo', verbose_name='Фото профиля'),
        ),
    ]