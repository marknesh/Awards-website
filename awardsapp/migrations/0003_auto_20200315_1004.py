# Generated by Django 3.0.3 on 2020-03-15 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awardsapp', '0002_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='awardsapp.Profile'),
        ),
    ]
