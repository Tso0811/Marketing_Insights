# Generated by Django 5.2.1 on 2025-05-25 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_campaigns_click'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaigns',
            old_name='title',
            new_name='name',
        ),
    ]
