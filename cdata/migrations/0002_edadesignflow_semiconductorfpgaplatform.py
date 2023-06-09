# Generated by Django 3.2.18 on 2023-06-04 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EDADesignFlow',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SemiconductorFPGAPlatform',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
