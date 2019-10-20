# Generated by Django 2.2.5 on 2019-10-04 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0002_auto_20190930_0030'),
    ]

    operations = [
        migrations.CreateModel(
            name='StorageVk',
            fields=[
                ('post_query', models.TextField()),
                ('post_link', models.TextField(primary_key=True, serialize=False)),
                ('post_id', models.TextField()),
                ('post_date', models.TextField()),
                ('post_owner', models.TextField()),
                ('post_text', models.TextField()),
                ('post_score', models.TextField()),
                ('post_keyword', models.TextField()),
                ('post_mark', models.TextField()),
                ('post_len', models.TextField()),
                ('post_category', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Storage',
        ),
    ]
