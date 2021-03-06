# Generated by Django 2.0.7 on 2018-08-12 14:55

from django.db import migrations

def populate_districttype(apps, schema_editor):
    
    DistrictType=apps.get_model('sdcpeople', 'DistrictType')

    DistrictType.objects.bulk_create([
        DistrictType(name='Borough', order=2),
        DistrictType(name='Precinct', order=3),
        DistrictType(name='Congressional', order=4),
        DistrictType(name='State Senate', order=5),
        DistrictType(name='State House', order=6),
        DistrictType(name='Magisterial', order=7),
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('sdcpeople', '0001_initial')
    ]

    operations = [
        migrations.RunPython(populate_districttype)
    ]
