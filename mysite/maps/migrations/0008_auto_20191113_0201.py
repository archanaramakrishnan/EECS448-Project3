# Generated by Django 2.1.5 on 2019-11-13 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0007_auto_20191111_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='building1',
            field=models.CharField(choices=[[1, 'Wescoe Hall'], [2, 'Budig Hall'], [3, 'LEEP2'], [4, 'Learned Hall'], [5, 'Fraser Hall']], max_length=255),
        ),
        migrations.AlterField(
            model_name='map',
            name='building2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='map',
            name='building3',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='map',
            name='building4',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='map',
            name='building5',
            field=models.CharField(max_length=255),
        ),
    ]
