# Generated by Django 2.2.5 on 2019-10-09 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0010_auto_20191009_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('stat_date', models.TextField(primary_key=True, serialize=False)),
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
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('post_query', models.TextField()),
                ('post_type', models.TextField()),
                ('post_ownert', models.TextField()),
                ('post_date', models.TextField()),
                ('post_link', models.TextField(primary_key=True, serialize=False)),
                ('post_id', models.TextField()),
                ('post_owner', models.TextField()),
                ('post_text', models.TextField()),
                ('post_score', models.TextField()),
                ('post_keyword', models.TextField()),
                ('post_mark', models.TextField()),
                ('post_len', models.TextField()),
                ('post_category', models.TextField()),
                ('post_textp', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='StatisticsVk',
        ),
        migrations.DeleteModel(
            name='StorageVK',
        ),
    ]
