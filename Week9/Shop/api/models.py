from django.db import models

class Category(models.Model):
    name =  models.CharField(max_length=200, db_index=True)

    def to_json(self):
        return {
            'category_id': self.id,
            'name': self.name
        }

class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    price = models.FloatField()
    description = models.TextField(blank=True)
    count = models.IntegerField(default=0)
    category_id = models.IntegerField()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'category_id': self.category_id
        }
