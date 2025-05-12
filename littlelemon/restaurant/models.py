from django.db import models

# Create your models here.

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return self.title

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.name
    
class MenuItem(models.Model):
#    Title = models.CharField(max_length=255, null=True)
#    Price = models.IntegerField(null=False) 
#    menu_item_description = models.TextField(max_length=1000, default='') 
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # inventory = models.SmallIntegerField(db_index=True, null=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} : {str(self.price)}'