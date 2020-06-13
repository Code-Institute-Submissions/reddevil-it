# Generated by Django 3.0.6 on 2020-06-11 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_profile_image'),
        ('store', '0025_auto_20200611_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='profile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='users.Profile'),
        ),
    ]