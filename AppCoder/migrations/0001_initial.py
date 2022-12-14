# Generated by Django 4.1 on 2022-09-26 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='billeteras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreBilletera', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Ejemplo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEjemplo', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='lentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreLentes', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Relojes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('modelo', models.IntegerField()),
            ],
        ),
    ]
