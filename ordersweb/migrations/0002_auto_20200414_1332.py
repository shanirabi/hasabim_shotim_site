# Generated by Django 3.0.2 on 2020-04-14 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
        ('ordersweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderWeb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address_line_1', models.CharField(max_length=120)),
                ('address_line_2', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(max_length=120)),
                ('country', models.CharField(default='ישראל', max_length=120)),
                ('postal_code', models.CharField(max_length=120)),
                ('status', models.CharField(choices=[('created', 'Created'), ('paid', 'Paid'), ('shipped', 'Shipped'), ('refunded', 'Refunded')], default='created', max_length=120)),
                ('shipping_cost', models.DecimalField(decimal_places=2, default=0, max_digits=100)),
                ('order_cost', models.DecimalField(decimal_places=2, default=0, max_digits=100)),
                ('total_cost', models.DecimalField(decimal_places=2, default=0, max_digits=100)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.Cart')),
            ],
        ),
        migrations.DeleteModel(
            name='Web_Order',
        ),
    ]
