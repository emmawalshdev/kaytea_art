# Generated by Django 3.2.6 on 2021-08-22 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20210821_2149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address_line1',
            new_name='street_address1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address_line2',
            new_name='street_address2',
        ),
    ]
