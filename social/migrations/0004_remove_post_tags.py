# Generated by Django 5.0.1 on 2024-02-07 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_post_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
    ]