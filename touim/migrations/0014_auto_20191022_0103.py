# Generated by Django 2.2.6 on 2019-10-21 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('touim', '0013_remove_mobiliers_is_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biblio',
            name='bib_logo',
        ),
        migrations.RemoveField(
            model_name='biblio',
            name='coll',
        ),
        migrations.RemoveField(
            model_name='biblio',
            name='edition',
        ),
        migrations.RemoveField(
            model_name='biblio',
            name='pages',
        ),
        migrations.RemoveField(
            model_name='biblio',
            name='tip',
        ),
    ]
