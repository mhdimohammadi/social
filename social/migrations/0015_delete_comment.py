# Generated by Django 5.0.1 on 2024-03-07 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0014_post_active'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]