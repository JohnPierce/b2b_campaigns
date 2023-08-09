# Generated by Django 3.2.18 on 2023-07-18 14:01

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchy', '0002_auto_20230718_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companygrouphierarchy',
            name='confidence',
            field=models.DecimalField(choices=[(Decimal('0.0'), '0.0'), (Decimal('0.1'), '0.1'), (Decimal('0.2'), '0.2'), (Decimal('0.3'), '0.3'), (Decimal('0.4'), '0.4'), (Decimal('0.5'), '0.5'), (Decimal('0.6'), '0.6'), (Decimal('0.7'), '0.7'), (Decimal('0.8'), '0.8'), (Decimal('0.9'), '0.9'), (Decimal('1.0'), '1.0')], decimal_places=1, default=0.5, max_digits=2),
        ),
        migrations.AlterField(
            model_name='employeehierarchy',
            name='confidence',
            field=models.DecimalField(choices=[(Decimal('0.0'), '0.0'), (Decimal('0.1'), '0.1'), (Decimal('0.2'), '0.2'), (Decimal('0.3'), '0.3'), (Decimal('0.4'), '0.4'), (Decimal('0.5'), '0.5'), (Decimal('0.6'), '0.6'), (Decimal('0.7'), '0.7'), (Decimal('0.8'), '0.8'), (Decimal('0.9'), '0.9'), (Decimal('1.0'), '1.0')], decimal_places=1, default=0.5, max_digits=2),
        ),
    ]