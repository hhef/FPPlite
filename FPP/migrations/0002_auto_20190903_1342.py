# Generated by Django 2.2.5 on 2019-09-03 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FPP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]