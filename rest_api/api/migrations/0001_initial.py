# Generated by Django 3.2.16 on 2022-11-10 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FilterData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TransactionData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField()),
                ('method', models.CharField(max_length=10)),
                ('url', models.CharField(max_length=50)),
                ('status_code', models.IntegerField()),
                ('latency', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='UsageData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu', models.FloatField()),
                ('ram', models.IntegerField()),
            ],
        ),
    ]