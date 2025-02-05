from django.db import models

from user_management.models import Profile

# Create your models here

class Commission(models.Model):
    COMMISSION_STATUS=[
        ('O', 'Open'),
        ('F', 'Full'),
        ('C', 'Completed'),
        ('D', 'Discontinued')   
    ]
    title = models.CharField(max_length=2555)
    description = models.TextField(max_length=255)
    status = models.CharField(max_length=1, choices=COMMISSION_STATUS, default='O')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='owner'
    )

    def __str__(self):
        return self.title
    class Meta: 
        ordering = ['created_on']

    

class Job(models.Model):
    JOB_STATUS = [
        ('O', 'Open'),
        ('F', 'Full')
    ]
    role = models.TextField()
    people_required = models.IntegerField()
    status = models.CharField(max_length=1,choices=JOB_STATUS,default='O')
    commission = models.ForeignKey(
        'Commission',
        on_delete=models.CASCADE,
        related_name='jobs',
        blank=True
    )

    def __str__(self):
        return self.role
    
    class Meta:
        ordering = ['-status', '-people_required', 'role']

class JobApplication(models.Model):
    APPLICATION_STATUS=[
        ('P', 'Pending'),
        ('A', 'Accepted'),
        ('R', 'Rejected')
    ]
    status=models.CharField(max_length=1, choices=APPLICATION_STATUS, default='P')
    applied_on=models.DateTimeField(auto_now_add=True)
    applicant=models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='job'
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name='applicant'
    )

    def __str__(self):
        return f"{self.job.role} applied by {self.applicant.user.username} is {self.get_status_display()}"
    
    class Meta:
        ordering = ['-status', '-applied_on']
