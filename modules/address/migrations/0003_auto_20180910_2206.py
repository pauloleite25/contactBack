# Generated by Django 2.1 on 2018-09-11 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20180910_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(blank=True, db_column='street', max_length=500, null=True),
        ),
    ]
