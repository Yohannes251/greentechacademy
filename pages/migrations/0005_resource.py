# Generated by Django 4.2.6 on 2023-10-31 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_rename_challanges_report_challenges'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.URLField(max_length=300)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]
