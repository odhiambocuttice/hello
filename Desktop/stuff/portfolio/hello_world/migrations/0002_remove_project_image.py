# Generated by Django 2.2.2 on 2019-06-06 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
    ]