# Generated by Django 4.2.5 on 2023-10-07 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TaskAPI', '0003_alter_task_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='completed',
            new_name='status',
        ),
    ]
