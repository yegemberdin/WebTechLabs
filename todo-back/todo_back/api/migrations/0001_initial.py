# Generated by Django 2.2 on 2019-04-14 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateField()),
                ('due_on', models.DateField()),
                ('status', models.CharField(max_length=200)),
                ('task_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.TaskList')),
            ],
        ),
    ]
