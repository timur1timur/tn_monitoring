# Generated by Django 2.2.5 on 2019-10-09 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0009_auto_20191009_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatisticsVk',
            fields=[
                ('stat_date', models.TextField(primary_key=True, serialize=False)),
                ('stat_count', models.TextField()),
                ('stat_social', models.TextField()),
                ('stat_media', models.TextField()),
                ('stat_common', models.TextField()),
                ('stat_tna', models.TextField()),
                ('stat_sport', models.TextField()),
                ('stat_fin', models.TextField()),
                ('stat_kvn', models.TextField()),
                ('stat_azs', models.TextField()),
                ('stat_adv', models.TextField()),
                ('stat_event', models.TextField()),
                ('stat_vak', models.TextField()),
                ('stat_warning', models.TextField()),
                ('stat_danger', models.TextField()),
                ('stat_secondary', models.TextField()),
                ('stat_success', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Statistics',
        ),
    ]