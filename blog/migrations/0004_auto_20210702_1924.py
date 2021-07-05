# Generated by Django 3.2.5 on 2021-07-02 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210702_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='user',
        ),
        migrations.AddField(
            model_name='event',
            name='author',
            field=models.CharField(default='Equipo Biblioteca Bayer', max_length=50, verbose_name='Autor'),
        ),
    ]
