# Generated by Django 2.0 on 2018-02-19 12:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0008_auto_20180219_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='last_edited_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]