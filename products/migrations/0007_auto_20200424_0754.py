# Generated by Django 3.0.2 on 2020-04-24 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_ml'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ml',
            field=models.IntegerField(blank=True, default='750', null=True),
        ),
    ]
