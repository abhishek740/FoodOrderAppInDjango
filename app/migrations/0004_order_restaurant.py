# Generated by Django 3.2.5 on 2021-08-03 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='restaurant',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
