# Generated by Django 3.2.5 on 2021-07-06 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_article_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='subcomision',
            field=models.ManyToManyField(default='Equipo Biblioteca Bayer', to='blog.SubCom', verbose_name='Subcomision'),
        ),
    ]