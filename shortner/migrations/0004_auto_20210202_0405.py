# Generated by Django 3.1.6 on 2021-02-01 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0003_auto_20210202_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='krikurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]
