# Generated by Django 3.0.6 on 2020-07-01 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0003_auto_20200701_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apoderado',
            old_name='nombre_completo_apoderado',
            new_name='nombre_completo',
        ),
        migrations.AlterField(
            model_name='contrato',
            name='id_contrato',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
