# Generated by Django 3.2.5 on 2021-07-14 19:00

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_event_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=80, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='subcom',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Descripcion'),
        ),
    ]