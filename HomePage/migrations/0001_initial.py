# Generated by Django 3.2.7 on 2022-03-20 13:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('id_number', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_requested', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved', models.BooleanField(default=False)),
                ('Dr_Name', models.CharField(choices=[('Dr. LIM', 'Dr. LIM'), ('Dr. Meledez', 'Dr. Meledez')], default=' ', max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id_number', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('date_recorded', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescribed_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('prescription_notes', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomePage.patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomePage.patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date_commented', models.DateTimeField(default=django.utils.timezone.now)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomePage.patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.FloatField()),
                ('payment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomePage.patient')),
            ],
        ),
        migrations.CreateModel(
            name='HealthHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomePage.patient')),
            ],
        ),
    ]
