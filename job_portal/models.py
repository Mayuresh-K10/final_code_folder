from django.db import models # type: ignore
from django.utils import timezone # type: ignore
from django.contrib.auth.models import User

class Job(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    description = models.TextField()
    requirements = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    experience_yr = models.CharField(max_length=10, default="0-100")
    job_title = models.CharField(max_length=200)
    job_type = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    category =models.CharField(max_length=100)
    skills = models.CharField(max_length=1000, blank= False, null=False)
    workplaceTypes = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    questions = models.TextField(blank=True, null=True)
    job_status = models.CharField(max_length=50, default='active')
    email = models.EmailField(null=False, default="unknown@example.com")
    must_have_qualification = models.BooleanField(default=False)
    filter = models.BooleanField(default=False)
    source = models.CharField(max_length=50,default='LinkedIn')
    card_number = models.CharField(max_length=20, blank=True, null=True, default='Not Provided') # Credit/Debit card number
    expiration_code = models.CharField(max_length=5, blank=True, null=True, default='MM/YY') # Expiration code (MM/YY)
    security_code = models.CharField(max_length=4, blank=True, null=True, default='000') # Security code
    country = models.CharField(max_length=100, blank=True, null=True, default='India') # Country
    postal_code = models.CharField(max_length=10, blank=True, null=True, default='000000') # Postal code
    gst = models.CharField(max_length=15, blank=True, null=True, default='Not Provided') # GST number
    promoting_job  =  models.BooleanField(default=False)
    first_name = models.CharField(max_length=255, null=False, default="John")
    last_name = models.CharField(max_length=255, null=False, default="Doe")

    def __str__(self):
        return self.job_title


class Application(models.Model):
    job = models.ForeignKey('Job', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=False, default="John")
    last_name = models.CharField(max_length=255, null=False, default="Doe")
    email = models.EmailField(null=False, default="unknown@example.com")
    phone_number = models.CharField(max_length=15, default="123-456-7890")
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(default="No cover letter provided")
    applied_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, default='pending')
    skills = models.CharField(max_length=1000, blank= False, null=False)

    def __str__(self):
        return f"{self.first_name} - {self.job.job_title}"

class Company(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(default='example@example.com')
    phone = models.CharField(max_length=20, default='000-000-0000')
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='India')
    zipcode = models.CharField(max_length=6, default='522426')
    website = models.URLField()
    website_urls = models.CharField(max_length=100, default='Unknown')
    about_company = models.CharField(max_length=255,default='about_company')
    sector_type = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default='Unknown')
    established_date = models.DateField(null=True, blank=True)
    employee_size = models.IntegerField(default=0)
    Attachment = models.FileField(upload_to='attachments/',default='Unknown')
    is_deleted  = models.BooleanField(default=False)


    def _str_(self):
        return self.name

class Resume(models.Model):
    first_name = models.CharField(max_length=100, default='John')
    last_name = models.CharField(max_length=100, default='John Doe')
    email = models.EmailField(default='example@example.com')
    phone = models.CharField(max_length=20, default='000-000-0000')
    address = models.TextField(default='N/A')
    date_of_birth = models.DateField(null=True, blank=True)
    website_urls = models.JSONField(default=list)  
    skills = models.TextField(default='Not specified')
    activities = models.TextField(default='None')
    interests = models.TextField(default='None')
    languages = models.TextField(default='None')
    bio = models.TextField(default='None')
    city = models.CharField(max_length=100, default='Mumbai')
    state = models.CharField(max_length=100, default='Maharashtra')
    country = models.CharField(max_length=100, default='India')
    zipcode = models.CharField(max_length=6, default='522426')
    Attachment = models.FileField(upload_to='attachments/',default='Unknown')
    delete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Objective(models.Model):
    resume = models.OneToOneField(Resume, related_name='objective', on_delete=models.CASCADE)
    text = models.TextField(default='Not specified')

class Education(models.Model):
    resume = models.ForeignKey(Resume, related_name='education_entries', on_delete=models.CASCADE, default=1)
    course_or_degree = models.CharField(max_length=100, default='Unknown')
    school_or_university = models.CharField(max_length=100, default='Unknown')
    grade_or_cgpa = models.CharField(max_length=50, default='N/A')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.course_or_degree} at {self.school_or_university}"

class Experience(models.Model):
    resume = models.ForeignKey(Resume, related_name='experience_entries', on_delete=models.CASCADE,default=1)
    job_title = models.CharField(max_length=100, default='Unknown')
    company_name = models.CharField(max_length=100, default='Unknown')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(default='No description')

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

class Project(models.Model):
    resume = models.ForeignKey(Resume, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='Untitled Project')
    description = models.TextField(default='No description')

    def __str__(self):
        return self.title

class Reference(models.Model):
    resume = models.ForeignKey(Resume, related_name='references', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='Unknown')
    contact_info = models.CharField(max_length=100, default='Not provided')
    relationship = models.CharField(max_length=100, default='N/A')

    def __str__(self):
        return self.name

class Certification(models.Model):
   resume = models.ForeignKey(Resume, related_name='certifications', on_delete=models.CASCADE)
   name = models.CharField(max_length=100, default='Unknown')
   start_date = models.DateField(null=True, blank=True)
   end_date = models.DateField(null=True, blank=True)
 
class Achievements(models.Model):
    resume = models.ForeignKey(Resume, related_name='achievements', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='Unknown')
    publisher = models.CharField(max_length=100, default='Unknown')
    date_of_issue = models.DateField(null=True, blank=True)

class Publications(models.Model):
    resume = models.ForeignKey(Resume, related_name='publications', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='Unknown')
    publisher = models.CharField(max_length=100, default='Unknown')
    date_of_publications = models.DateField(null=True, blank=True)

class CandidateStatus_selected(models.Model):
    first_name = models.CharField(max_length=255,default='John')
    last_name = models.CharField(max_length=255,default='Doe')
    status = models.CharField(max_length=20,default='selected')
    company_name = models.CharField(max_length=255)
    job_id = models.IntegerField()

class CandidateStatus_rejected(models.Model):
    first_name = models.CharField(max_length=255,default='John')
    last_name = models.CharField(max_length=255,default='Doe')
    status = models.CharField(max_length=20,default='rejected')
    company_name = models.CharField(max_length=255)
    job_id = models.IntegerField()

class CandidateStatus_not_eligible(models.Model):
    first_name = models.CharField(max_length=255,default='John')
    last_name = models.CharField(max_length=255,default='Doe')
    status = models.CharField(max_length=20,default='not_eligible')
    company_name = models.CharField(max_length=255)
    job_id = models.IntegerField()

class CandidateStatus_under_review(models.Model):
    first_name = models.CharField(max_length=255,default='John')
    last_name = models.CharField(max_length=255,default='Doe')
    status = models.CharField(max_length=20,default='under_review')
    company_name = models.CharField(max_length=255)
    job_id = models.IntegerField()

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='recipient', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender.email} -> {self.recipient.email}"

    class Meta:
        ordering = ['timestamp']

class Attachment(models.Model):
    message = models.ForeignKey('Message', related_name='attachments', on_delete=models.CASCADE)
    file = models.FileField(upload_to='attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attachment for message {self.message.id}"

class Student(models.Model):
    first_name =  models.CharField(max_length=100, default='John')
    last_name = models.CharField(max_length=100, default='Doe')
    email = models.EmailField(default='example@example.com')
    contact_no = models.CharField(max_length=20, default='000-000-0000')
    qualification = models.TextField(default='N/A')
    skills = models.TextField(default='Not specified')

# class MembershipPlan(models.Model):
#     PLAN_CHOICES = [
#         ('Standard', 'Standard'),
#         ('Gold', 'Gold'),
#         ('Diamond', 'Diamond'),
#     ]

#     name = models.CharField(max_length=50, choices=PLAN_CHOICES)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     job_postings = models.IntegerField()
#     featured_jobs = models.IntegerField()
#     post_duration = models.IntegerField(help_text="Job post live duration in days")

#     def __str__(self):
#         return self.name

# class UserSubscription(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     current_plan = models.ForeignKey(MembershipPlan, on_delete=models.SET_NULL, null=True, blank=True)
#     subscription_date = models.DateTimeField(default=timezone.now)
#     renewal_date = models.DateTimeField()

#     def is_active(self):
#         return timezone.now() < self.renewal_date

#     def __str__(self):
#         return f'{self.user.username} - {self.current_plan.name}'


class ScreeningQuestion(models.Model):
    job = models.ForeignKey(Job, related_name='screening_questions', on_delete=models.CASCADE)
    question_text = models.TextField()
    correct_answer = models.TextField()

    def __str__(self):
        return self.question_text[:50]

class ScreeningAnswer(models.Model):
    application = models.ForeignKey(Application, related_name='screening_answers', on_delete=models.CASCADE)
    question = models.ForeignKey(ScreeningQuestion, related_name='answers', on_delete=models.CASCADE)
    answer_text = models.TextField()

    def __str__(self):
        return f"Answer for {self.question.question_text[:50]}"


