# Generated by Django 2.2 on 2021-08-08 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bigbox', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name_plural': 'Activities'},
        ),
        migrations.AlterModelOptions(
            name='box',
            options={'verbose_name_plural': 'Boxes'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
