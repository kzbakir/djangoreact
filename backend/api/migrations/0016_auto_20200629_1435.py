# Generated by Django 2.2.7 on 2020-06-29 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20200620_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battle',
            name='user1Round1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='battle',
            name='user1Round2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='battle',
            name='user1Round3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='battle',
            name='user1Round4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='battle',
            name='user2Round1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='battle',
            name='user2Round2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='battle',
            name='user2Round3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='battle',
            name='user2Round4',
            field=models.TextField(blank=True, null=True),
        ),
    ]
