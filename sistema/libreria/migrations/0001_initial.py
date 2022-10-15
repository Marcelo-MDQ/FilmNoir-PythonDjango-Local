# Generated by Django 4.1 on 2022-08-30 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('anio', models.IntegerField()),
                ('imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen')),
            ],
        ),
    ]
