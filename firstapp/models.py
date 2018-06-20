from django.db import models
 
class Person(models.Model):
    i_ru = models.CharField(max_length=20)
    ip = models.CharField(max_length=20)
    tip = models.CharField(max_length=20)
    descript = models.CharField(max_length=20)
    prim = models.CharField(max_length=20)
    vlan_byfly = models.CharField(max_length=20)
    pool_iptv = models.CharField(max_length=20)
    pool_tr069 = models.CharField(max_length=20)
    ims_relay = models.CharField(max_length=20)
    hw_access = models.CharField(max_length=20)
    ohr_dhcp = models.CharField(max_length=20)
    imssignaling = models.CharField(max_length=20)
    imsmedia = models.CharField(max_length=20)
    numbers = models.CharField(max_length=20)
 
class Rues(models.Model):
    name = models.CharField(max_length=20)

class Gmipadress(models.Model):
    name = models.CharField(max_length=20)


