# Generated by Django 2.0.4 on 2018-05-12 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_profile_followed_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='followed_categories',
        ),
    ]
