# Generated by Django 4.0.6 on 2022-07-24 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('befit_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=15),
        ),
    ]