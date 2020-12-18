# Generated by Django 3.1.4 on 2020-12-18 08:16

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
            name='WorkerCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WorkingArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='WorkerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('working_Time', models.CharField(blank=True, max_length=100, null=True)),
                ('hourly_rate', models.FloatField(blank=True, null=True)),
                ('extra_service', models.CharField(blank=True, max_length=250, null=True)),
                ('experience', models.FloatField(blank=True, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('views', models.PositiveIntegerField(blank=True, default=0)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pic/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.workercategory')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='worker_profile', to=settings.AUTH_USER_MODEL)),
                ('working_area', models.ManyToManyField(to='accounts.WorkingArea')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.IntegerField()),
                ('message', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worker_message', to='accounts.workerprofile')),
            ],
        ),
    ]
