# Generated by Django 2.2.2 on 2019-06-23 19:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PanelsForGame', '0005_auto_20190624_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personagetransfer',
            name='date_last_visit',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 24, 2, 28, 10, 878173), help_text='Последняя дата визита локации'),
        ),
    ]