# Generated by Django 3.0.5 on 2020-10-22 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_orderproduct'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='consumer',
            options={'verbose_name': 'Consumer', 'verbose_name_plural': 'Consumers'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['category']},
        ),
        migrations.AlterModelOptions(
            name='provider',
            options={'verbose_name': 'Provider', 'verbose_name_plural': 'Providers'},
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
    ]
