# Generated by Django 3.0.2 on 2020-04-29 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordersweb', '0009_orderweb_approve_terms'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderweb',
            old_name='age_above_18',
            new_name='approve_terms_and_age_above_18',
        ),
        migrations.RemoveField(
            model_name='orderweb',
            name='approve_terms',
        ),
    ]
