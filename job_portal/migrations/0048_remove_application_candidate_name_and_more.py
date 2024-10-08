# Generated by Django 4.2.15 on 2024-09-18 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0047_job_email_job_filter_job_must_have_qualification_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='candidate_name',
        ),
        migrations.AddField(
            model_name='application',
            name='first_name',
            field=models.CharField(default='John', max_length=255),
        ),
        migrations.AddField(
            model_name='application',
            name='last_name',
            field=models.CharField(default='Doe', max_length=255),
        ),
        migrations.AddField(
            model_name='job',
            name='card_number',
            field=models.CharField(blank=True, default='Not Provided', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='country',
            field=models.CharField(blank=True, default='India', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='expiration_code',
            field=models.CharField(blank=True, default='MM/YY', max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='gst',
            field=models.CharField(blank=True, default='Not Provided', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='postal_code',
            field=models.CharField(blank=True, default='000000', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='security_code',
            field=models.CharField(blank=True, default='000', max_length=4, null=True),
        ),
    ]
