# Generated by Django 4.2 on 2024-09-15 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_owner_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('in', 'In'), ('out', 'Out')], max_length=50)),
                ('description', models.TextField(blank=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_status', to='core.car')),
            ],
        ),
    ]