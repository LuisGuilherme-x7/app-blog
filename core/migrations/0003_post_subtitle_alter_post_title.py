# Generated by Django 4.1.2 on 2022-10-24 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Subtitulo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Titulo'),
        ),
    ]
