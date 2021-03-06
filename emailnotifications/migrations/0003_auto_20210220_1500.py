# Generated by Django 3.1.6 on 2021-02-20 15:00

from django.db import migrations, models
import emailnotifications.validators


class Migration(migrations.Migration):

    dependencies = [
        ('emailnotifications', '0002_auto_20210220_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useremails',
            name='email_ID',
            field=models.EmailField(max_length=254, unique=True, validators=[emailnotifications.validators.validate_Email]),
        ),
    ]
