# Generated by Django 5.1 on 2024-09-21 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0003_alter_clothingmodel_options_alter_clothingmodel_desc_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ClothingModel',
        ),
        migrations.DeleteModel(
            name='Rubric',
        ),
    ]