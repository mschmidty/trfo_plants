# Generated by Django 3.0 on 2019-12-14 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0004_auto_20191214_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant_basics',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]