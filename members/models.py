from django.db import models
from django.contrib import auth

class Character(models.Model):
    """
    Represends Eve characters. They are fetched via API and stored
    here in the DB. Inactive characters are only visible to a
    director. A new entry is created when it's first seen by the API
    and inactivated when it is no longer available via API.  Chars
    without user ids are also inactive.
    """
    ACTIVE_STATES = (
        (0, u'inactive'),
        (1, u'active'),
        (2, u'always_active'))
    eve_char_id = models.IntegerField() # eve character id
    eve_char_name = models.CharField(max_length=45) # eve character name
    user = models.ForeignKey(auth.models.User) # django user id
    monthly_fee = models.DecimalField(max_digits=9, decimal_places=2) # corp monthly membership fee for this character
    is_active = models.IntegerField(choices=ACTIVE_STATES) # only active characters are displayed

    def __unicode__(self):
        return "%s (%d): %s" & (self.eve_char_name, self.eve_char_id, self.is_active)

class Booking(models.Model):
    """
    Represents a single booking of membership fee. The money_source is
    either the character, or the corporation (e.g. during trial phase
    the corp pays the fee).
    """
    MONEY_SOURCE = (
        (1, u'corp'),
        (2, u'member'))
    character = models.ForeignKey(Character)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    booking_date = models.DateTimeField()
    money_source = models.IntegerField(choices=MONEY_SOURCE)

    def __unicode__(self):
        return "%d: %s -> %.2f" % (self.eve_char_id, self.money_source, self.amount)
