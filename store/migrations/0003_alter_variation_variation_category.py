# Generated by Django 5.0.6 on 2024-06-24 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('Color', 'color'), ('Size', 'size')], max_length=100),
        ),
    ]
