# Generated by Django 2.2.1 on 2022-11-08 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pograncontrol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=3)),
                ('cause', models.CharField(max_length=100)),
                ('vus', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('kpp', models.CharField(max_length=50)),
                ('yService', models.CharField(max_length=15)),
                ('voenk', models.CharField(max_length=50)),
                ('kategory', models.CharField(max_length=3)),
                ('katZ', models.CharField(max_length=1)),
                ('date', models.DateField()),
            ],
        ),
    ]