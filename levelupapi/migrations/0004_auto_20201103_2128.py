# Generated by Django 3.1.2 on 2020-11-03 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0003_game_maker'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='game_type',
            new_name='gametype',
        ),
    ]
