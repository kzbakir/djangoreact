# Generated by Django 2.2.7 on 2020-06-20 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_remove_profile_is_online'),
    ]

    operations = [
        migrations.RenameField(
            model_name='battle',
            old_name='user1Result',
            new_name='user1Total',
        ),
        migrations.RenameField(
            model_name='battle',
            old_name='user2Result',
            new_name='user2Total',
        ),
        migrations.AddField(
            model_name='battle',
            name='result',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='user1Round1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='user1Round2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='user1Round3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='user1Round4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='user2Round1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='user2Round2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='user2Round3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='user2Round4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='school',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='battle',
            name='started',
            field=models.IntegerField(default=1),
        ),
    ]
