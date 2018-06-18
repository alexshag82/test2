from django import forms
 
class UserForm(forms.Form):
    i_ru = forms.CharField(min_length=2, max_length=20)
    ipadr = forms.CharField(min_length=2, max_length=20)
    val_tip = forms.CharField(min_length=2, max_length=20)
    va2_desc = forms.CharField(min_length=2, max_length=20)
    va3_prim = forms.CharField(min_length=2, max_length=20)
    va4_vlan_byfly = forms.CharField(min_length=2, max_length=20)
    va5_pool_iptv = forms.CharField(min_length=2, max_length=20)
    va6_pool_tr069 = forms.CharField(min_length=2, max_length=20)
    va7_ims_relay = forms.CharField(min_length=2, max_length=20)
    va8_hwf = forms.CharField(min_length=2, max_length=20)
    va9_ohr = forms.CharField(min_length=2, max_length=20)
    va10_imssignal = forms.CharField(min_length=2, max_length=20)
    val1_imsmedia = forms.CharField(min_length=2, max_length=20)
    val2_nomers = forms.CharField(min_length=2, max_length=20)
