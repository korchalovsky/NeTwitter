# Generated by Django 3.0.7 on 2020-06-20 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NeTwitter', '0006_article_article_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NeTwitter.Profile'),
        ),
    ]
