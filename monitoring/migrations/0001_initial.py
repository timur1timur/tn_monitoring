# Generated by Django 2.2.5 on 2019-09-29 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_query', models.TextField()),
                ('post_link', models.TextField()),
                ('post_id', models.TextField()),
                ('post_date', models.TextField()),
                ('post_owner', models.TextField()),
                ('post_text', models.TextField()),
                ('post_score', models.TextField()),
                ('post_keyword', models.TextField()),
                ('post_mark', models.TextField()),
                ('post_len', models.TextField()),
            ],
        ),
    ]
