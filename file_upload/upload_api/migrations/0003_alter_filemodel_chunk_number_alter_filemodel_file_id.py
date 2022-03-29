# Generated by Django 4.0.3 on 2022-03-29 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_api', '0002_filemodel_chunk_number_filemodel_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='chunk_number',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='file_id',
            field=models.CharField(max_length=20),
        ),
    ]
