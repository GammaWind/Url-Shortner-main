# Generated by Django 3.1.6 on 2021-02-21 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emailnotifications', '0003_auto_20210220_1500'),
        ('shortner', '0008_auto_20210221_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='krikurl',
            name='createdBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emailnotifications.useremails'),
            
        ),
    ]
