from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmusica', '0003_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('contenido', models.CharField(max_length=40)),
                ('imagen', models.URLField()),
                ('autor', models.CharField(max_length=40)),
            ],
        ),
    ]
