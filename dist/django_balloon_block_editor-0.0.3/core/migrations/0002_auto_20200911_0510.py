# Generated by Django 3.1.1 on 2020-09-11 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='content',
        ),
        migrations.AddField(
            model_name='test',
            name='test',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]