# Generated by Django 5.1.1 on 2024-09-26 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_attendance_date_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date_check',
            field=models.CharField(default='26.09.2024 07:38', max_length=100),
        ),
    ]
