# Generated by Django 3.1.1 on 2021-04-27 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0014_auto_20210427_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorders',
            name='orders',
            field=models.TextField(default=None),
        ),
    ]
