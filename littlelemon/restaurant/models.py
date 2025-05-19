from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=100)
    no_of_guests = models.PositiveIntegerField()
    bookingDate = models.DateField()
    
    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Booking Records'

    def __str__(self):
        return f"{self.name} - {self.bookingDate}"

class Menu(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu Items'

    def __str__(self):
        return f'{self.title} : {str(self.price)}'

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    groups = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.username} : {str(self.email)}'