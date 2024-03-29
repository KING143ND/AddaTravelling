# Generated by Django 3.2 on 2022-10-16 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_auto_20221015_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='hotel_desc1',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_desc2',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_desc3',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_desc4',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_desc5',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_desc6',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_image1',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_image2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_image3',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_image4',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_image5',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_image6',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_price1',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_price2',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_price3',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_price4',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_price5',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_price6',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_rating1',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_rating2',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_rating3',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_rating4',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_rating5',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_rating6',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_title1',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_title2',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_title3',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_title4',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_title5',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_title6',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
