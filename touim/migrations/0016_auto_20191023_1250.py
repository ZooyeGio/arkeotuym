# Generated by Django 2.2.6 on 2019-10-23 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touim', '0015_auto_20191022_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='biblio',
            name='coll',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='biblio',
            name='edition',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='biblio',
            name='pages',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='biblio',
            name='tip',
            field=models.CharField(default='', max_length=50),
        ),
    ]
