# Generated by Django 4.0.1 on 2022-04-30 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0003_customer_alter_user_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
