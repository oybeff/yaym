# Generated by Django 5.0.7 on 2024-08-22 19:36

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mind', '0008_alter_articlein_related_article_alter_team_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='story_of_member'),
        ),
        migrations.CreateModel(
            name='Teamin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='', verbose_name='img_of_person')),
                ('related_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mind.team')),
            ],
        ),
    ]
