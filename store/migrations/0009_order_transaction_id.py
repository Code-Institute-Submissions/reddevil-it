# Generated by Django 3.0.6 on 2020-06-04 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_remove_order_transaction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(editable=False, max_length=32, null=True),
        ),
    ]