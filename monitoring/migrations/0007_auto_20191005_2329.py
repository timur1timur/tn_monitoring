# Generated by Django 2.2.5 on 2019-10-05 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0006_remove_storagevk_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storagevk',
            name='post_date',
            field=models.TextField(),
        ),
    ]
