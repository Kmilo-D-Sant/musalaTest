# Generated by Django 4.1.1 on 2023-06-06 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Image'),
        ),
    ]
