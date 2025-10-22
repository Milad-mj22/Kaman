from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class PhoneLead(models.Model):
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)




class CompanySize(models.Model):
    size_name = models.CharField(max_length=100)

    def __str__(self):
        return self.size_name

class BusinessArea(models.Model):
    area_name = models.CharField(max_length=100)

    def __str__(self):
        return self.area_name
    


class DemoUser(models.Model):
    phone = models.CharField(max_length=15,unique=True)

    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    company_size = models.ForeignKey('CompanySize', on_delete=models.SET_NULL, null=True, blank=True)
    business_area = models.ForeignKey('BusinessArea', on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} {self.last_name}"