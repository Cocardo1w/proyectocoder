# Generated by Django 4.0.3 on 2022-05-11 16:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appmusica', '0007_alter_entrada_contenido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('contenido', models.TextField(max_length=800)),
                ('autor', models.CharField(max_length=40)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='appmusica.entrada')),
            ],
        ),
    ]
