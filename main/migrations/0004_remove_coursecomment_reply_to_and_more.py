# Generated by Django 4.2.2 on 2023-11-21 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_course_category_remove_course_sub_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursecomment',
            name='reply_to',
        ),
        migrations.RemoveField(
            model_name='lessoncomment',
            name='reply_to',
        ),
    ]