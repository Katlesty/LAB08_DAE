# Generated by Django 5.0.6 on 2024-05-08 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0002_categoria_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
    ]
