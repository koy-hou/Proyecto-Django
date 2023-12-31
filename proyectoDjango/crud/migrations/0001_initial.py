# Generated by Django 4.2.1 on 2023-06-28 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=50, verbose_name='Genero')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha actualización')),
            ],
            options={
                'verbose_name': 'Genero',
                'verbose_name_plural': 'Generos',
                'ordering': ['genero'],
            },
        ),
        migrations.CreateModel(
            name='Recomendacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recomendacion', models.CharField(max_length=50, verbose_name='Recomendacion')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha actualización')),
            ],
            options={
                'verbose_name': 'Recomendacion',
                'verbose_name_plural': 'Recomendaciones',
                'ordering': ['recomendacion'],
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('idAlbum', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Titulo')),
                ('artista', models.CharField(max_length=100, verbose_name='Artista')),
                ('analisis', models.CharField(max_length=20000, verbose_name='Analisis')),
                ('image', models.ImageField(blank=True, null=True, upload_to='albums', verbose_name='Imagen')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha actualización')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.genero', verbose_name='Genero')),
                ('recomendacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.recomendacion', verbose_name='Recomendacion')),
            ],
            options={
                'verbose_name': 'album',
                'verbose_name_plural': 'albums',
                'ordering': ['title', 'idAlbum'],
            },
        ),
    ]
