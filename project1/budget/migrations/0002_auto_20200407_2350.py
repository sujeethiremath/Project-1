# Generated by Django 2.2.5 on 2020-04-07 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='Actual',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='budget',
            name='Projected',
            field=models.PositiveIntegerField(),
        ),
    ]