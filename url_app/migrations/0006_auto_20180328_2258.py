# Generated by Django 2.0.2 on 2018-03-28 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_app', '0005_auto_20180328_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshortener',
            name='url',
            field=models.URLField(max_length=300),
        ),
    ]
