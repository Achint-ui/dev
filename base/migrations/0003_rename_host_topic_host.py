# Generated by Django 5.1 on 2024-10-05 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_topic_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='Host',
            new_name='host',
        ),
    ]
