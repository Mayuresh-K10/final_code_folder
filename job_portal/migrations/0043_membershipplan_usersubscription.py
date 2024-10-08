# Generated by Django 4.2.15 on 2024-09-17 09:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0042_rename_delete_company_is_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Standard', 'Standard'), ('Gold', 'Gold'), ('Diamond', 'Diamond')], max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('job_postings', models.IntegerField()),
                ('featured_jobs', models.IntegerField()),
                ('post_duration', models.IntegerField(help_text='Job post live duration in days')),
            ],
        ),
        migrations.CreateModel(
            name='UserSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('renewal_date', models.DateTimeField()),
                ('current_plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='job_portal.membershipplan')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='job_portal.user')),
            ],
        ),
    ]
