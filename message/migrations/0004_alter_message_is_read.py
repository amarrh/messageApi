# Generated by Django 3.2.7 on 2021-09-19 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_alter_message_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='is_read',
            field=models.BooleanField(auto_created=True, default=False),
        ),
    ]
