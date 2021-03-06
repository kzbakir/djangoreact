# Generated by Django 2.2.7 on 2020-04-23 16:50

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20200423_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battle',
            name='questions',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='battle',
            name='user1Answers',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='battle',
            name='user1Result',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='battle',
            name='user2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='battle',
            name='user2Answers',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='battle',
            name='user2Result',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
