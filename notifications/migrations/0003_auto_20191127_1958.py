# Generated by Django 2.2.7 on 2019-11-27 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20191125_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='humidity',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='ppm',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='temperature',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='type',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='notification',
            name='velocity',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
