# Generated by Django 3.2.8 on 2021-10-10 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]
