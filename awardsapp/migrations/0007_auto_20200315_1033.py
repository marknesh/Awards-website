# Generated by Django 3.0.3 on 2020-03-15 10:33

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('awardsapp', '0006_auto_20200315_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='project_link',
            field=tinymce.models.HTMLField(),
        ),
    ]
