# Generated by Django 4.1.2 on 2022-11-01 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_post_subtitle_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', editable=False, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default='', max_length=500, verbose_name='Subtitulo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=200, verbose_name='Titulo'),
        ),
    ]
