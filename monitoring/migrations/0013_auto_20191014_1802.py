# Generated by Django 2.2.5 on 2019-10-14 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0012_auto_20191010_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics1',
            fields=[
                ('stat_id', models.TextField(primary_key=True, serialize=False)),
                ('stat_date', models.DateField()),
                ('stat_count', models.TextField()),
                ('stat_comment', models.TextField()),
                ('stat_post', models.TextField()),
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