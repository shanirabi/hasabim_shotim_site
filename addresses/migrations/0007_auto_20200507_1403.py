# Generated by Django 3.0.2 on 2020-05-07 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0006_auto_20200318_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
