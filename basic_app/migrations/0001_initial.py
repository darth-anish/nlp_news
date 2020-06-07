# Generated by Django 2.2.12 on 2020-05-25 05:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2020, 5, 25, 5, 52, 53, 367077, tzinfo=utc))),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('text', models.TextField()),
            ],
        ),
    ]
