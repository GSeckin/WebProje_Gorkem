# Generated by Django 2.2.4 on 2019-11-21 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_alanlar'),
    ]

    operations = [
        migrations.AddField(
            model_name='alanlar',
            name='a3',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alanlar',
            name='a4',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
