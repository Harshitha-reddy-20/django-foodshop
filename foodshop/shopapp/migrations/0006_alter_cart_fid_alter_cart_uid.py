# Generated by Django 5.1.2 on 2024-10-24 08:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0005_cart'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='fid',
            field=models.ForeignKey(db_column='fid', on_delete=django.db.models.deletion.CASCADE, to='shopapp.fooditem'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='uid',
            field=models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
