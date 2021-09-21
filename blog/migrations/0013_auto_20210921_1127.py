# Generated by Django 3.2.6 on 2021-09-21 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210907_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='friendly_name',
            field=models.CharField(default='text', max_length=80),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='keyword',
            name='name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='reply',
            name='body',
            field=models.TextField(max_length=600),
        ),
    ]
