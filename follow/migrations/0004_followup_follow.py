# Generated by Django 3.2.18 on 2023-09-17 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follow', '0003_auto_20230812_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='followup',
            name='follow',
            field=models.BooleanField(default=False),
        ),
    ]