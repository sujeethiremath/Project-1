# Generated by Django 3.0.3 on 2020-04-14 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_taskcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcategory',
            name='Category',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.TaskCategory'),
        ),
    ]