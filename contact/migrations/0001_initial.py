# Generated by Django 3.0.2 on 2020-02-27 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('eaddress', models.EmailField(max_length=150)),
                ('tel', models.CharField(max_length=15)),
                ('message', models.TextField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
