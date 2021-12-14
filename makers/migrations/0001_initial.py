# Generated by Django 3.2.8 on 2021-10-09 09:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('expected_period_start', models.DateField(null=True)),
                ('expected_period_end', models.DateField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postion', models.CharField(choices=[('REQUESTED', 'requested for participation'), ('MEMBER', 'member'), ('ADMIN', 'admin who has permissions')], max_length=10)),
                ('progress_status', models.CharField(choices=[('WAITING', 'wating for open'), ('IN_PROGRESS', 'project is working on it'), ('DONE', 'project is done')], max_length=20)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL)),
                ('field', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='makers.field')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='makers.group')),
            ],
        ),
    ]
