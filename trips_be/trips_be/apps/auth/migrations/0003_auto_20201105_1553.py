# Generated by Django 3.1.2 on 2020-11-05 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_tourguide_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tourguide',
            old_name='guide',
            new_name='user',
        ),
    ]
