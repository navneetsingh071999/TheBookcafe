from django.db import models

class products(models.Model):
    bkname = models.CharField(max_length = 100)
    bkauth = models.CharField(max_length = 100)
    price = models.IntegerField()
    bkcatgory = models.CharField(max_length = 30)
    bkedtion = models.CharField(max_length = 30)
    seller_name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = 'pics')
    seller_address = models.CharField(max_length = 500)
    seller_email = models.CharField(max_length = 80)

