# Generated by Django 4.2.5 on 2024-07-04 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_variation_variation_category'),
        ('carts', '0002_rename_card_id_cart_cart_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.variation'),
        ),
    ]
