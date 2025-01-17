# Generated by Django 5.1.2 on 2024-10-23 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_fooditems_fdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='fooditem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Fooditem name')),
                ('price', models.FloatField()),
                ('fdetails', models.CharField(max_length=150, verbose_name='Description')),
                ('cat', models.IntegerField(choices=[(1, 'Biryani'), (2, 'Pizza'), (3, 'Burger'), (4, 'Desserts'), (5, 'South Indian')], verbose_name='Category')),
                ('is_active', models.BooleanField(default=True, verbose_name='Available')),
            ],
        ),
        migrations.DeleteModel(
            name='fooditems',
        ),
    ]
