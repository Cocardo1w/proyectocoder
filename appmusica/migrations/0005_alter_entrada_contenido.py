from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmusica', '0004_entrada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='contenido',
            field=models.TextField(max_length=400),
        ),
    ]

