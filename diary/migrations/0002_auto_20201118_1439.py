# Generated by Django 3.1.3 on 2020-11-18 05:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
