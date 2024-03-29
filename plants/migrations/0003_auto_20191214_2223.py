# Generated by Django 3.0 on 2019-12-14 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_remove_plant_basics_family'),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family', models.CharField(max_length=100)),
                ('family_description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='plant_basics',
            name='family',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='plants.Family'),
        ),
    ]
