# Generated by Django 3.2.5 on 2021-07-19 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20210718_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalprojects',
            name='status',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='status',
        ),
    ]
