# Generated by Django 2.1.3 on 2019-01-04 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0011_auto_20181127_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='attachment',
            field=models.FileField(blank=True, max_length=254, upload_to='', verbose_name='Attachment'),
        ),
    ]
