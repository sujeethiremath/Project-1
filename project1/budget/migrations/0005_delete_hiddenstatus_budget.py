# Generated by Django 2.2.5 on 2020-04-08 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0004_auto_20200407_2356'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HiddenStatus_Budget',
        ),
    ]