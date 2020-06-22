# Generated by Django 3.0.7 on 2020-06-22 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NeTwitter', '0009_auto_20200621_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NeTwitter.Profile', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.CharField(max_length=1000, verbose_name='Текст статьи'),
        ),
    ]
