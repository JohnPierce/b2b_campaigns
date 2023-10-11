# Generated by Django 3.2.18 on 2023-09-25 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cdata', '0024_edasuppliertool'),
        ('design_flow', '0002_auto_20230917_0318'),
    ]

    operations = [
        migrations.AddField(
            model_name='companygroupedadesignflow',
            name='name_subcat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cdata.edadesignflowsubcategory'),
        ),
        migrations.AddField(
            model_name='companygroupedadesignflow',
            name='name_supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cdata.supplier'),
        ),
        migrations.AddField(
            model_name='companygroupedadesignflow',
            name='name_tool',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cdata.edasuppliertools'),
        ),
    ]