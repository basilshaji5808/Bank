# Generated by Django 4.1.1 on 2023-02-03 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banksite_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='ac_type',
            field=models.CharField(choices=[('Savings Account', 'Savings Account'), ('Current Account', 'Current Account')], max_length=100),
        ),
    ]
