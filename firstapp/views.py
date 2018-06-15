from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Person
 
# получение данных из бд
def index(request):
    people = Person.objects.all()
    return render(request, "index.html", {"people": people})
 
# сохранение данных в бд
def create(request):
    if request.method == "POST":
        person = Person()
        person.ipadr = request.POST.get("ipadr")
        person.val_tip = request.POST.get("val_tip")
        person.va2_desc = request.POST.get("va2_desc")
        person.va3_prim = request.POST.get("va3_prim")
        person.va4_vlan_byfly = request.POST.get("va4_vlan_byfly")
        person.va5_pool_iptv = request.POST.get("va5_pool_iptv")
        person.va6_pool_tr069 = request.POST.get("va6_pool_tr069")
        person.va7_ims_relay = request.POST.get("va7_ims_relay")
        person.va8_hwf = request.POST.get("va8_hwf")
        person.va9_ohr = request.POST.get("va9_ohr")
        person.va10_imssignal = request.POST.get("va10_imssignal")
        person.val1_imsmedia = request.POST.get("val1_imsmedia")
        person.val2_nomers = request.POST.get("val2_nomers")
        person.save()
    return HttpResponseRedirect("/")
 
# изменение данных в бд
def edit(request, id):
    try:
        person = Person.objects.get(id=id)
 
        if request.method == "POST":
            person.ipadr = request.POST.get("ipadr")
            person.val_tip = request.POST.get("val_tip")
            person.va2_desc = request.POST.get("va2_desc")
            person.va3_prim = request.POST.get("va3_prim")
            person.va4_vlan_byfly = request.POST.get("va4_vlan_byfly")
            person.va5_pool_iptv = request.POST.get("va5_pool_iptv")
            person.va6_pool_tr069 = request.POST.get("va6_pool_tr069")
            person.va7_ims_relay = request.POST.get("va7_ims_relay")
            person.va8_hwf = request.POST.get("va8_hwf")
            person.va9_ohr = request.POST.get("va9_ohr")
            person.va10_imssignal = request.POST.get("va10_imssignal")
            person.val1_imsmedia = request.POST.get("val1_imsmedia")
            person.val2_nomers = request.POST.get("val2_nomers")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
     
# удаление данных из бд
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")