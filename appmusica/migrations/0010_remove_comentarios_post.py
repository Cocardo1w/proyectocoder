# Generated by Django 4.0.3 on 2022-05-11 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmusica', '0009_remove_comentarios_autor_remove_comentarios_fecha_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentarios',
            name='post',
        ),
    ]