# Generated by Django 3.1 on 2021-03-06 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_auto_20210306_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auctionlist',
            old_name='state',
            new_name='status',
        ),
    ]
