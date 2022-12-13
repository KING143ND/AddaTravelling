# Generated by Django 3.2 on 2022-10-16 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_auto_20221016_2121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='cleanliness',
            new_name='cleanliness1',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='comfort',
            new_name='cleanliness2',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='facilities',
            new_name='comfort1',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='reviews',
            new_name='comfort2',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='value_for_money',
            new_name='facilities1',
        ),
        migrations.AddField(
            model_name='hotel',
            name='facilities2',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='hotel',
            name='reviews1',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='hotel',
            name='reviews2',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='hotel',
            name='value_for_money1',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='hotel',
            name='value_for_money2',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
    ]
