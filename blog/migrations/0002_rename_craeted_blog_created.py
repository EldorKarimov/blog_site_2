# Generated by Django 4.0.4 on 2022-05-05 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='craeted',
            new_name='created',
        ),
    ]