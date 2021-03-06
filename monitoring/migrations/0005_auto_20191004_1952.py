# Generated by Django 2.2.5 on 2019-10-04 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0004_auto_20191004_1943'),
    ]

    operations = [
        migrations.CreateModel(
            name='StorageVK',
            fields=[
                ('post_query', models.TextField()),
                ('post_link', models.TextField(primary_key=True, serialize=False)),
                ('post_type', models.TextField()),
                ('post_id', models.TextField()),
                ('post_owner', models.TextField()),
                ('post_text', models.TextField()),
                ('post_score', models.TextField()),
                ('post_keyword', models.TextField()),
                ('post_mark', models.TextField()),
                ('post_len', models.TextField()),
                ('post_category', models.TextField()),
                ('post_date', models.DateTimeField()),
                ('post_time', models.DateTimeField()),
                ('post_textp', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='StorageVKpost',
        ),
    ]
