# Generated by Django 5.2 on 2025-04-16 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0006_alter_controle_entrada_alter_controle_saida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controle',
            name='entrada',
            field=models.TimeField(verbose_name='Entrada'),
        ),
    ]
