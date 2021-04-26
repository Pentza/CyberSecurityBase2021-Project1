# Generated by Django 3.1.7 on 2021-04-25 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=150)),
                ('receiver', models.CharField(max_length=150)),
                ('message_content', models.CharField(max_length=400)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
