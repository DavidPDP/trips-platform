# Generated by Django 3.1.2 on 2020-11-07 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20201105_1811'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tourguide',
            old_name='userId',
            new_name='user',
        ),
    ]