# Generated by Django 3.1.6 on 2021-02-08 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Polls',
            new_name='Polls_table',
        ),
    ]