# Generated by Django 5.0.8 on 2024-09-03 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_imagen_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='imagen',
            field=models.ImageField(default='imagenes/avatar1.jpg', upload_to='imagenes'),
        ),
    ]