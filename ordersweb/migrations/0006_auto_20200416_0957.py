# Generated by Django 3.0.2 on 2020-04-16 09:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ordersweb', '0005_auto_20200416_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderweb',
            name='delivery_method',
            field=models.CharField(blank=True, choices=[('pickup', 'איסוף עצמי'), ('shipping', 'משלוח בתשלום')], max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='orderweb',
            name='order_submitted_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderweb',
            name='pickup_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orderweb',
            name='shipping_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderweb',
            name='status',
            field=models.CharField(blank=True, choices=[('created', 'Created'), ('paid', 'Paid'), ('shipped', 'Shipped'), ('created', 'Created'), ('refunded', 'Refunded')], default='created', max_length=120, null=True),
        ),
    ]
