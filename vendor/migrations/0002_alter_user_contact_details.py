# Generated by Django 4.2.8 on 2023-12-09 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact_details',
            field=models.TextField(blank=True, null=True),
        ),
    ]
