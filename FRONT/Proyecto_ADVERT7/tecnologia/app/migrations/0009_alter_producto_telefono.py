# Generated by Django 3.2.6 on 2021-09-08 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_producto_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='telefono',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
