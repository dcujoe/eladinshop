from django.db import models
from django.db.models.signals import pre_save

# Create your models here.
# the default models are groups and users, Categories is created as a new custom model
class Category(models.Model):
# name of category
    category_name = models.CharField(max_length=50, unique=True)
# unique url of the category
    slug = models.CharField(max_length=100, unique=True)
# description of the category_name, store category image if __name__ == '__main__':
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories/', blank=True)

# class to change the name of category from categorys to categories
    class Meta:
        verbose_name = 'category'

        verbose_name_plural = 'categories'

def _str_(self):
    return self.category_name
from django.db.models.signals import pre_save

def ready(self):
    # importing model classes
    from .models import MyModel  # or...
    MyModel = self.get_model('MyModel')

    # registering signals with the model's string label
    pre_save.connect(receiver, sender='app_label.MyModel')
