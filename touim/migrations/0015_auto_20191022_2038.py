# Generated by Django 2.2.6 on 2019-10-22 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touim', '0014_auto_20191022_0103'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='biblio',
            options={'ordering': ('titre',)},
        ),
        migrations.RemoveField(
            model_name='biblio',
            name='site',
        ),
        migrations.AddField(
            model_name='sites',
            name='biblio',
            field=models.ManyToManyField(to='touim.Biblio'),
        ),
    ]
