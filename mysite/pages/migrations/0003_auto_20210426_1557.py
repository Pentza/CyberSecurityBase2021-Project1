# Generated by Django 3.1.7 on 2021-04-26 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_remove_message_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_content',
            field=models.TextField(),
        ),
    ]
