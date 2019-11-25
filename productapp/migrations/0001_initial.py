# Generated by Django 2.2.6 on 2019-11-08 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('pcat', models.CharField(max_length=20)),
                ('pname', models.CharField(max_length=20)),
                ('pcost', models.DecimalField(decimal_places=4, max_digits=10)),
                ('pdisc', models.DecimalField(decimal_places=4, max_digits=10)),
                ('pmfdt', models.DateField()),
                ('pexpdt', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('prodid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='productapp.Product')),
                ('tot_qty', models.IntegerField()),
                ('last_update', models.DateField()),
                ('next_update', models.DateField()),
            ],
        ),
    ]