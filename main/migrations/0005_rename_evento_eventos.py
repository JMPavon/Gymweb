# Generated by Django 4.2.6 on 2023-10-20 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_evento_delete_eventos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Evento',
            new_name='Eventos',
        ),
    ]
