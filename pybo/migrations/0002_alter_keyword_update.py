# Generated by Django 3.2.6 on 2021-09-09 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='update',
            field=models.CharField(max_length=256),
        ),
    ]
