# Generated by Django 5.0.6 on 2024-06-21 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_category_auctionlisting_bid_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='watched_by', to='auctions.auctionlisting'),
        ),
    ]
