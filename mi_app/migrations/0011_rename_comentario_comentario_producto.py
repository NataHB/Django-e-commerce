# Generated by Django 5.0.8 on 2024-09-06 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mi_app', '0010_alter_comentario_nombre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='comentario',
            new_name='producto',
        ),
    ]