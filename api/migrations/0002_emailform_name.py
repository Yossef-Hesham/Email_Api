# Generated by Django 5.1.6 on 2025-03-05 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailform',
            name='name',
            field=models.CharField(default='unknown', max_length=50),
        ),
    ]
