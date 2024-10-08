# Generated by Django 4.2.15 on 2024-09-18 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0046_remove_company_job_status_job_job_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='email',
            field=models.EmailField(default='unknown@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='job',
            name='filter',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='must_have_qualification',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='source',
            field=models.CharField(default='LinkedIn', max_length=50),
        ),
        migrations.CreateModel(
            name='ScreeningQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screening_questions', to='job_portal.job')),
            ],
        ),
        migrations.CreateModel(
            name='ScreeningAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField()),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screening_answers', to='job_portal.application')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='job_portal.screeningquestion')),
            ],
        ),
    ]
