# Generated by Django 4.2.6 on 2023-10-22 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_companiainfo_remove_sucursal_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companiainfo',
            name='urlLogo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]