# Generated by Django 4.2.15 on 2024-09-20 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0053_message_attachment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersubscription',
            name='current_plan',
        ),
        migrations.RemoveField(
            model_name='usersubscription',
            name='user',
        ),
        migrations.DeleteModel(
            name='MembershipPlan',
        ),
        migrations.DeleteModel(
            name='UserSubscription',
        ),
    ]
