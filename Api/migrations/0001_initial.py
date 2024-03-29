# Generated by Django 4.1.1 on 2023-06-06 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dron',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serialNumber', models.CharField(max_length=100, verbose_name='Serial number')),
                ('model', models.CharField(choices=[('Lightweight', 'Lightweight'), ('Middleweight', 'Middleweight'), ('Cruiserweight', 'Cruiserweight'), ('Heavyweight', 'Heavyweight')], max_length=50, verbose_name='Model')),
                ('weightLimit', models.FloatField(verbose_name='Weigh limit')),
                ('battery', models.IntegerField(verbose_name='Battery')),
                ('state', models.CharField(choices=[('IDLE', 'IDLE'), ('LOADING', 'LOADING'), ('LOADED', 'LOADED'), ('DELIVERING', 'DELIVERING'), ('DELIVERED', 'DELIVERED'), ('RETURNING', 'RETURNING')], max_length=50, verbose_name='State')),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('weight', models.FloatField(verbose_name='Weight')),
                ('code', models.CharField(max_length=100, verbose_name='Code')),
                ('image', models.CharField(max_length=100, verbose_name='Image')),
            ],
        ),
    ]
