# Generated by Django 3.1.7 on 2021-04-26 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20210426_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.TextField(),
        ),
    ]
