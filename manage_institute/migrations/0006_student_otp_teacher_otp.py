# Generated by Django 5.0.6 on 2024-06-03 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_institute', '0005_delete_forgot'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='otp',
            field=models.CharField(default='000000', max_length=10),
        ),
        migrations.AddField(
            model_name='teacher',
            name='otp',
            field=models.CharField(default='000000', max_length=10),
        ),
    ]
