from django.db import models
 
class Person(models.Model):
    ipadr = models.CharField(max_length=20)
    val_tip = models.CharField(max_length=20)
    va2_desc = models.CharField(max_length=20)
    va3_prim = models.CharField(max_length=20)
    va4_vlan_byfly = models.CharField(max_length=20)
    va5_pool_iptv = models.CharField(max_length=20)
    va6_pool_tr069 = models.CharField(max_length=20)
    va7_ims_relay = models.CharField(max_length=20)
    va8_hwf = models.CharField(max_length=20)
    va9_ohr = models.CharField(max_length=20)
    va10_imssignal = models.CharField(max_length=20)
    val1_imsmedia = models.CharField(max_length=20)
    val2_nomers = models.CharField(max_length=20)
