# Generated by Django 2.0.4 on 2018-05-11 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20180511_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedpage',
            name='followed_categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Category'),
        ),
        migrations.AlterField(
            model_name='feedpage',
            name='followed_questions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Question'),
        ),
        migrations.AlterField(
            model_name='feedpage',
            name='followed_users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TheFollowings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='feedpage',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='TheUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
