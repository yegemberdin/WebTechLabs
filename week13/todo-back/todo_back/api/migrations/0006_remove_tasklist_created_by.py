# Generated by Django 2.2 on 2019-04-29 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190430_0532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasklist',
            name='created_by',
        ),
    ]
