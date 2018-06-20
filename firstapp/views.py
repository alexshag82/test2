from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Rues
from .models import Person

 
# получение данных из бд
def index(request):
    # q = Entry.objects.filter(headline__startswith="What")
    # q = q.filter(pub_date__lte=datetime.now())
    # q = q.exclude(body_text__icontains="food")
    name_rues = Rues.objects.all()
    ipadress = Person.objects.all()
    # ipadress = Person.objects.filter(ipadr="192.168.201.30")
    # ipadress = Person.objects.filter(ipadr__startswith="192.168.201.")
    # ipadress_202 = Person.objects.filter(ipadr__startswith="192.168.202.")
    return render(request, "index.html", {"name_rues": name_rues, "ipadress": ipadress})

def gm_ipadr(request):
    # q = Entry.objects.filter(headline__startswith="What")
    # q = q.filter(pub_date__lte=datetime.now())
    # q = q.exclude(body_text__icontains="food")
    name_rues = Rues.objects.all()
    ipadress = Person.objects.all()
    # ipadress = Person.objects.filter(ipadr="192.168.201.30")
    # ipadress = Person.objects.filter(ipadr__startswith="192.168.201.")
    # ipadress_202 = Person.objects.filter(ipadr__startswith="192.168.202.")
    return render(request, "gm_ipadr.html", {"name_rues": name_rues, "ipadress": ipadress})

def list(request, id):
    # q = Entry.objects.filter(headline__startswith="What")
    # q = q.filter(pub_date__lte=datetime.now())
    # q = q.exclude(body_text__icontains="food")
    name_rues = Rues.objects.all()
    ipadress = Person.objects.all()
    # ipadress = Person.objects.filter(ipadr="192.168.201.30")
    # ipadress = Person.objects.filter(ipadr__startswith="192.168.201.")
    # ipadress_202 = Person.objects.filter(ipadr__startswith="192.168.202.")
    return render(request, "list.html", {"name_rues": name_rues, "ipadress": ipadress, "id": id})

# изменение данных в бд
def edit(request, id):
    try:
        person = Person.objects.get(id=id)
 
        if request.method == "POST":
            person.i_ru = request.POST.get("i_ru")
            person.ip = request.POST.get("ip")
            person.tip = request.POST.get("tip")
            person.descript = request.POST.get("descript")
            person.prim = request.POST.get("prim")
            person.vlan_byfly = request.POST.get("vlan_byfly")
            person.pool_iptv = request.POST.get("pool_iptv")
            person.pool_tr069 = request.POST.get("pool_tr069")
            person.ims_relay = request.POST.get("ims_relay")
            person.hw_access = request.POST.get("hw_access")
            person.ohr_dhcp = request.POST.get("ohr_dhcp")
            person.imssignaling = request.POST.get("imssignaling")
            person.imsmedia = request.POST.get("imsmedia")
            person.numbers = request.POST.get("numbers")
            person.save()
            return HttpResponseRedirect("/list/"+person.i_ru+"/")
        else:
            return render(request, "edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
     
# удаление данных из бд
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.i_ru = request.POST.get("i_ru")
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
