from django.db import models
from django.db.models import CharField, TextField, FloatField


class Company(models.Model):
    name = CharField(max_length=200)
    description = TextField(default='')
    city = CharField(max_length=200)
    address = TextField(blank=True)

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
    description = TextField(default='')
    salary = FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name = 'vacancies')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary
        }
