# Generated by Django 3.0.2 on 2020-03-18 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_symbol', models.IntegerField()),
                ('city_name_hebrew', models.CharField(max_length=240, unique=True)),
                ('city_name_english', models.CharField(max_length=240)),
                ('city_name_transcription', models.CharField(max_length=240)),
                ('district', models.CharField(max_length=240)),
                ('subdistrict_name', models.CharField(max_length=240)),
                ('subdistrict_symbol', models.IntegerField()),
                ('data_year', models.IntegerField(default='2018')),
            ],
        ),
    ]
