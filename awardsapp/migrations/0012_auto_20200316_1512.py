# Generated by Django 3.0.3 on 2020-03-16 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awardsapp', '0011_projects_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='project_link',
            field=models.TextField(),
        ),
    ]