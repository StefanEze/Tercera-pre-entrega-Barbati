# Generated by Django 4.1.7 on 2023-03-14 18:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('WebDjango', '0003_rename_nombre_articulo_nombres'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='nombres',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='fecha_de_nacimiento',
        ),
        migrations.AddField(
            model_name='articulo',
            name='nombre',
            field=models.CharField(default=django.utils.timezone.now, max_length=35),
            preserve_default=False,
        ),
    ]