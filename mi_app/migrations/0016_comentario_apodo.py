# Generated by Django 5.0.8 on 2024-09-06 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_app', '0015_remove_comentario_usuario_alter_comentario_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='apodo',
            field=models.CharField(default='Anonimo', max_length=40),
        ),
    ]