# Generated by Django 3.1.2 on 2020-11-03 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0002_auto_20201030_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='maker',
            field=models.CharField(default='', max_length=55),
        ),
    ]