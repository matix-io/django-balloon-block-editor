# Generated by Django 3.1.1 on 2020-09-11 05:02

import balloon_block_editor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', balloon_block_editor.fields.BalloonBlockEditorField()),
            ],
        ),
    ]
