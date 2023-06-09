# Generated by Django 3.2.18 on 2023-07-01 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cdata', '0012_auto_20230701_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeHierarchy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cdata.company')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='cdata.contact')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hierarchy.employeehierarchy')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyGroupHierarchy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cdata.company')),
                ('company_group', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='cdata.companygroup')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hierarchy.companygrouphierarchy')),
            ],
        ),
    ]
