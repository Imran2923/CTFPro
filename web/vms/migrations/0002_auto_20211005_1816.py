# Generated by Django 2.2.12 on 2021-10-05 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='stat_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='status',
            name='component',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vms.Components'),
        ),
    ]
