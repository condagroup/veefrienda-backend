# Generated by Django 2.2.2 on 2019-06-20 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190618_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='belong_to',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='소속'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='생년월일'),
        ),
    ]
