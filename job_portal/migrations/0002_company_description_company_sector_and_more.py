# Generated by Django 4.2.11 on 2024-07-24 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.CharField(default='DEFAULT VALUE', max_length=255),
        ),
        migrations.AddField(
            model_name='company',
            name='sector',
            field=models.CharField(default='DEFAULT VALUE', max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('selected', 'Selected'), ('not_selected', 'Not Selected'),
                            ('not_eligible', 'Not Eligible'), ('under_review', 'under_review')], default='pending', max_length=20),
        ),
    ]
