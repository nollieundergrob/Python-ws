# Generated by Django 5.1.1 on 2024-09-20 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liveStream', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='group',
            field=models.CharField(max_length=100),
        ),
    ]
