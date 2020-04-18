from django.contrib.auth.models import User
from django.db import models
from django.db.models import CharField, FloatField

class CompanyManager(models.Manager):
    def for_user_order_by_name(self, user):
        return self.filter(created_by=user).order_by('name')

class Company(models.Model):
    name = CharField(max_length=200)
    description = CharField(max_length=200)
    city = CharField(max_length=200)
    address = CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=2)

    objects = CompanyManager()

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

class Vacancy(models.Model):
    name = CharField(max_length=200)
    description = CharField(max_length=200)
    salary = FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name = 'vacancies')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary
        }
