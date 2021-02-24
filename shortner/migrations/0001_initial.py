# Generated by Django 3.1.6 on 2021-02-24 16:03

from django.db import migrations, models
import django.db.models.deletion
import shortner.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('emailnotifications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Krikurl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=220, validators=[shortner.validators.validate_url, shortner.validators.validate_url_com])),
                ('shortcode', models.CharField(blank=True, max_length=15, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emailnotifications.useremails')),
            ],
        ),
    ]
