# Generated by Django 3.2.9 on 2021-12-21 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0014_auto_20211221_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.TextField(default='a', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.TextField(default='a'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.TextField(default='male', max_length=50),
            preserve_default=False,
        ),
    ]
