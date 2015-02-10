from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.IntegerField(primary_key=True,)
    name = models.TextField()
    price = models.IntegerField()
    category = models.IntegerField()

    class Meta(object):
        db_table = 'product'


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.TextField()

    class Meta(object):
        db_table = 'category'


