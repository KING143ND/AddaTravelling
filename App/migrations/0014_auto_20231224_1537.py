# Generated by Django 3.2 on 2023-12-24 10:07

from django.db import migrations

def revert_place_titles(apps, schema_editor):
    Place = apps.get_model('App', 'Place')

    for place in Place.objects.all():
        place.place_title = ' '.join(place.place_title.split('+'))
        place.save()

class Migration(migrations.Migration):

    dependencies = [
        ('App', '0013_place_image_url'),
    ]

    operations = [
        migrations.RunPython(revert_place_titles),
    ]
