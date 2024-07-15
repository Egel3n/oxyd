# Generated by Django 5.0.4 on 2024-07-08 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QueryLogPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EventDate', models.DateTimeField()),
                ('DatebaseID', models.IntegerField()),
                ('Hostname', models.CharField(max_length=30)),
                ('AppName', models.CharField(max_length=30)),
                ('SessionID', models.IntegerField()),
                ('UserName', models.CharField(max_length=30)),
                ('SqlText', models.CharField(max_length=30)),
                ('Duration', models.IntegerField()),
            ],
        ),
    ]
