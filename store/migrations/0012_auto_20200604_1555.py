# Generated by Django 3.0.6 on 2020-06-04 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20200604_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipping',
            name='email',
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
