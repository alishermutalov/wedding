# Generated by Django 5.1.1 on 2024-10-04 11:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wedding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groom_name', models.CharField(max_length=100)),
                ('bride_name', models.CharField(max_length=100)),
                ('groom_info', models.TextField(blank=True, null=True)),
                ('bride_info', models.TextField(blank=True, null=True)),
                ('wedding_date', models.DateTimeField()),
                ('vanue_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('invitation_style', models.CharField(blank=True, max_length=255, null=True)),
                ('qr_code_style', models.CharField(blank=True, max_length=255, null=True)),
                ('donation_card_number', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
