# Generated by Django 2.2.5 on 2020-04-07 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_budget_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='Username',
            field=models.CharField(max_length=100),
        ),
    ]
