# Generated by Django 3.2.4 on 2022-03-19 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]