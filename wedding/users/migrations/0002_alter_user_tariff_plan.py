# Generated by Django 5.1.1 on 2024-10-16 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tariff_plan',
            field=models.CharField(blank=True, choices=[('basic', 'basic'), ('standard', 'standard'), ('premium', 'premium')], max_length=20, null=True),
        ),
    ]
