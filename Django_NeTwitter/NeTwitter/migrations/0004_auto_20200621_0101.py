# Generated by Django 3.0.7 on 2020-06-20 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NeTwitter', '0003_auto_20200621_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]
