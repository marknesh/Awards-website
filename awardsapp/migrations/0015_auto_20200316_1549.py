# Generated by Django 3.0.3 on 2020-03-16 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awardsapp', '0014_auto_20200316_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='project_link',
            field=models.CharField(default='User', max_length=30),
        ),
    ]