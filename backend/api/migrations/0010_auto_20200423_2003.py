# Generated by Django 2.2.7 on 2020-04-23 14:03

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20200423_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battle',
            name='questions',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
        migrations.AlterField(
            model_name='battle',
            name='user1Answers',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
        migrations.AlterField(
            model_name='battle',
            name='user2Answers',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
    ]