# Generated by Django 4.1.1 on 2022-09-16 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(default='', max_length=12),
            preserve_default=False,
        ),
    ]
