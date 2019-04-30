# Generated by Django 2.2 on 2019-04-29 23:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_tasklist_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
