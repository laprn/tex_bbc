# Generated by Django 3.1.3 on 2020-11-18 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_auto_20201118_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='title',
            field=models.CharField(max_length=40, verbose_name='Title'),
        ),
    ]
