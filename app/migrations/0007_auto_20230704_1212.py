# Generated by Django 3.2.19 on 2023-07-04 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_num_ad_cart_uid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad_cart',
            old_name='uid',
            new_name='num',
        ),
        migrations.AlterField(
            model_name='ad_cart',
            name='quantity',
            field=models.IntegerField(max_length=255),
        ),
    ]
