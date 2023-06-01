from copy import copy

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Core(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    coins = models.IntegerField(default=0)
    click_power = models.IntegerField(default=1)

    def click(self):
        self.coins +=self.click_power

        if self.coins >= self.check_lvl_price():
            self.level +=1
            return True

        return False
    def check_lvl_price(self):
        return (self.level ** 2 +1) * 100 (self.level + 1)

class Boost(models.Model):
    core = models.ForeignKey(Core, null=False, on_delete=models.CASCADE)
    lvl = models.IntegerField(default=1)
    price = models.IntegerField(default=10)
    power = models.IntegerField(default=1)

    def levelup(self):
        if self.price > self.core.coins:
            return False
        old_boost_ststs = copy(self)
        self.core.coins -= self.price
        self.core.click_power += self.power
        self.core.save()

        self.lvl += 1
        self.power *=2
        self.price *=10
        self.save()

        return  old_boost_ststs, self