# Generated by Django 3.1.1 on 2021-04-19 17:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0002_auto_20210419_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorders',
            name='discount',
            field=models.CharField(blank=True, max_length=3, null=True, validators=[django.core.validators.RegexValidator(regex='^[1-9]$')]),
        ),
        migrations.AlterField(
            model_name='customerorders',
            name='reason_for_cancel',
            field=models.TextField(blank=True, null=True),
        ),
    ]
