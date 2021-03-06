# Generated by Django 3.0.3 on 2020-03-15 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awardsapp', '0008_auto_20200315_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='profile_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='awardsapp.Profile'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
