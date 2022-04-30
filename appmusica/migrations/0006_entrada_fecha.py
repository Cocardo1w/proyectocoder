from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appmusica', '0005_alter_entrada_contenido'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

