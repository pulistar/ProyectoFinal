# Generated by Django 5.0.4 on 2024-05-02 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='peliculas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('sinopsis', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('actores', models.CharField(max_length=100)),
                ('fecha_estreno', models.IntegerField()),
                ('duracion', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('sinopsis', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('actores', models.CharField(max_length=100)),
                ('fecha_estreno', models.IntegerField()),
                ('temporada', models.IntegerField()),
                ('duracion', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]