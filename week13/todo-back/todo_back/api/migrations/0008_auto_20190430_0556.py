# Generated by Django 2.2 on 2019-04-29 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_tasklist_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasklist',
            old_name='created_by',
            new_name='createed',
        ),
    ]
