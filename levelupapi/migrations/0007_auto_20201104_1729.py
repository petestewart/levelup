# Generated by Django 3.1.2 on 2020-11-04 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0006_auto_20201104_1725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='gamer',
            new_name='organizer',
        ),
    ]
