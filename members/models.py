from django.db import models

class Character(models.Model):
    eve_char_id = models.IntegerField()
    user_id = models.ForeignKey(models.User)
    monthly_fee = models.DecimalField(max_digits=9 decimal_places=2)

class Booking(models.Model):
    eve_char_id = models.ForeignKey(Character)
    amount = models.DecimalField(max_digits=9 decimal_places=2)
    booking_date = models.DateTimeField()
    
