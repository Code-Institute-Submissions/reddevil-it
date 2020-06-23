# Generated by Django 3.0.6 on 2020-06-23 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0035_order_member_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.CharField(choices=[('S', 'SM'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], default='', max_length=2),
        ),
    ]
