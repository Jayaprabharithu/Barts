# Generated by Django 5.0.6 on 2024-07-24 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bartsapp', '0004_projectdb_image4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdb',
            name='Finished_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectdb',
            name='Started_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]