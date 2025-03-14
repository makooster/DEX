# Generated by Django 5.1.6 on 2025-03-12 07:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auto', '0003_alter_auto_mileage_alter_auto_year'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CarDetailOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('canceled', 'Canceled')], default='pending', max_length=20)),
                ('comment', models.TextField(blank=True, null=True)),
                ('response_data', models.JSONField(blank=True, null=True)),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details_requests', to='auto.auto')),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
