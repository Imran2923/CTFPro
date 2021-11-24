# Generated by Django 2.2.12 on 2021-10-05 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='components',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('components_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_text', models.CharField(max_length=200)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vms.components')),
            ],
        ),
    ]
