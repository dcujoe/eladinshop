from django.db import models

# Create your models here.
class Category(models.Model):
# name of category
    category_name = models.CharField(max_length=50, unique=True)
# unique url of the category
    slug = models.CharField(max_length=100, unique=True)
# description of the category_name, store category image if __name__ == '__main__':
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories/', blank=True)

def _str_(self):
    return self.category_name
