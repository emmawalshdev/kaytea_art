# Generated by Django 3.2.6 on 2021-09-21 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0003_auto_20210912_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='commissions',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
