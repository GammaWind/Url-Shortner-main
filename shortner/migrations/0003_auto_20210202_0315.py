# Generated by Django 3.1.6 on 2021-02-01 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0002_auto_20210202_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='krikurl',
            name='shortcode',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
