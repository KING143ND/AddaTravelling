# Generated by Django 3.2 on 2022-09-24 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
