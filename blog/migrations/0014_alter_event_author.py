# Generated by Django 3.2.5 on 2021-07-26 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='author',
            field=models.CharField(default='La Bayer Band', max_length=50, verbose_name='Autor'),
        ),
    ]
