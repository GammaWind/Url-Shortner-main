# Generated by Django 3.1.6 on 2021-02-01 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0004_auto_20210202_0405'),
    ]

    operations = [
        migrations.AddField(
            model_name='krikurl',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
