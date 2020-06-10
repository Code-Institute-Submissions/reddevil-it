# Generated by Django 3.0.6 on 2020-06-06 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200521_1702'),
        ('store', '0014_remove_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_profile', to='users.Profile'),
        ),
    ]