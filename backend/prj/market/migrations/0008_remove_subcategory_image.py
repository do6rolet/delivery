# Generated by Django 3.0.5 on 2020-10-27 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_auto_20201027_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='image',
        ),
    ]