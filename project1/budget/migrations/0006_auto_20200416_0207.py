# Generated by Django 3.0.3 on 2020-04-16 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0005_delete_hiddenstatus_budget'),
    ]

    operations = [
        migrations.CreateModel(
            name='BudgetCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='budget',
            name='Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budget.BudgetCategory'),
        ),
    ]
