# Generated by Django 2.2.5 on 2019-10-17 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0023_auto_20191017_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='name',
            field=models.TextField(default=111),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='stat_date',
            field=models.TextField(default=111),
            preserve_default=False,
        ),
    ]