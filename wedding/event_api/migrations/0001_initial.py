# Generated by Django 5.1.1 on 2024-10-04 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wedding_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('background_image', models.ImageField(upload_to='event_images/')),
                ('wedding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='wedding_api.wedding')),
            ],
        ),
    ]
