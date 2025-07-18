from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    qr_code = models.TextField()
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    ATTENDANCE_STATUS = (
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
    )
    status = models.CharField(max_length=10, choices=ATTENDANCE_STATUS, default='Present')
    location_name = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    check_in = models.TimeField(blank=True, null=True)
    check_out = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.date} - {self.status} - {self.time} - {self.location_name}"
