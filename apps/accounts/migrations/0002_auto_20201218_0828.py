# Generated by Django 3.1.4 on 2020-12-18 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workerprofile',
            old_name='working_Time',
            new_name='working_time',
        ),
    ]