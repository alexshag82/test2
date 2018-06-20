from django import forms
 
class UserForm(forms.Form):
    i_ru = forms.CharField(min_length=2, max_length=20)
    ip = forms.CharField(min_length=2, max_length=20)
    tip = forms.CharField(min_length=2, max_length=20)
    descript = forms.CharField(min_length=2, max_length=20)
    prim = forms.CharField(min_length=2, max_length=20)
    vlan_byfly = forms.CharField(min_length=2, max_length=20)
    pool_iptv = forms.CharField(min_length=2, max_length=20)
    pool_tr069 = forms.CharField(min_length=2, max_length=20)
    ims_relay = forms.CharField(min_length=2, max_length=20)
    hw_access = forms.CharField(min_length=2, max_length=20)
    ohr_dhcp = forms.CharField(min_length=2, max_length=20)
    imssignaling = forms.CharField(min_length=2, max_length=20)
    imsmedia = forms.CharField(min_length=2, max_length=20)
    numbers = forms.CharField(min_length=2, max_length=20)
