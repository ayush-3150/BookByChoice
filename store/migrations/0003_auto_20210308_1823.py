# Generated by Django 3.1.5 on 2021-03-08 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210304_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='available_quantity',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='book',
            name='total_Stock',
            field=models.IntegerField(default=5),
        ),
    ]
