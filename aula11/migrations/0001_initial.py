# Generated by Django 2.2.10 on 2020-03-21 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=300)),
                ('numero', models.CharField(max_length=20)),
                ('bairro', models.CharField(max_length=20)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=2)),
                ('destino', models.CharField(max_length=300)),
                ('recebido_em', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Origem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=300)),
                ('numero', models.CharField(max_length=20)),
                ('bairro', models.CharField(max_length=20)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=2)),
                ('empresa', models.CharField(max_length=300)),
                ('enviado_em', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
