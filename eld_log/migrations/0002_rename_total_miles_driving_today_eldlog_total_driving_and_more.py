# Generated by Django 4.2.20 on 2025-03-18 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eld_log', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eldlog',
            old_name='Total_miles_driving_today',
            new_name='total_driving',
        ),
        migrations.RenameField(
            model_name='eldlog',
            old_name='totle_driving',
            new_name='total_miles_driving_today',
        ),
        migrations.RenameField(
            model_name='eldlog',
            old_name='totle_off_duty',
            new_name='total_off_duty',
        ),
        migrations.RenameField(
            model_name='eldlog',
            old_name='totle_on_duty',
            new_name='total_on_duty',
        ),
        migrations.RenameField(
            model_name='eldlog',
            old_name='totle_sleeper_berth',
            new_name='total_sleeper_berth',
        ),
    ]
