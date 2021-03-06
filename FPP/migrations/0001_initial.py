# Generated by Django 2.2.5 on 2019-09-03 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.FloatField(choices=[(1, 'Klient'), (2, 'Dostawca')])),
                ('name', models.CharField(max_length=256)),
                ('contact', models.TextField()),
                ('debt', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_for_sale', models.FloatField()),
                ('purchase_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=256)),
                ('quantity', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='FPP.Category')),
                ('price_for_sale', models.ManyToManyField(to='FPP.ProductHistory')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('amount', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='FPP.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.FloatField(choices=[(1, 'Dostawa'), (2, 'Sprzedaż')])),
                ('date', models.DateField()),
                ('amount', models.FloatField()),
                ('contractor', models.ManyToManyField(to='FPP.Contractor')),
                ('details', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='FPP.OrderDetail')),
            ],
        ),
    ]
