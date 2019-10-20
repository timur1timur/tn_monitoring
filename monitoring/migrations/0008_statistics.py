# Generated by Django 2.2.5 on 2019-10-09 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0007_auto_20191005_2329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat_date', models.TextField()),
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
    ]
