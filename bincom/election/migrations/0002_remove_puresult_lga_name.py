# Generated by Django 4.1.7 on 2023-03-26 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='puresult',
            name='lga_name',
        ),
    ]