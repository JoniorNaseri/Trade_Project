# Generated by Django 4.2.6 on 2023-10-30 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='failed_trades',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='successful_trades',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='total_trades',
        ),
    ]