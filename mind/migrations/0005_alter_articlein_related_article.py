# Generated by Django 5.0.7 on 2024-08-19 16:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mind', '0004_alter_articlein_related_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlein',
            name='related_article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mind.article'),
        ),
    ]