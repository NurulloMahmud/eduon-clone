# Generated by Django 4.2.6 on 2023-11-23 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_coursecomment_reply_to_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='video_location',
            field=models.FileField(upload_to='lessons/'),
        ),
    ]