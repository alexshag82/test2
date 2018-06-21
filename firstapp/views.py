from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Rues
from .models import Person
from .models import Gmipimsstatic

 
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

def gm_ipadr(request, id):
    # q = Entry.objects.filter(headline__startswith="What")
    # q = q.filter(pub_date__lte=datetime.now())
    # q = q.exclude(body_text__icontains="food")
    name_rues = Rues.objects.all()
    imsstat = Gmipimsstatic.objects.all()
    # ipadress = Person.objects.filter(ipadr="192.168.201.30")
    # ipadress = Person.objects.filter(ipadr__startswith="192.168.201.")
    # ipadress_202 = Person.objects.filter(ipadr__startswith="192.168.202.")
    return render(request, "gm_ipadr.html", {"name_rues": name_rues, "imsstat": imsstat, "id": id})

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
		
# изменение данных в бд
def edit_gm_ipadr(request, id):
    try:
        gmipimsstatic = Gmipimsstatic.objects.get(id=id)
 
        if request.method == "POST":
            gmipimsstatic.i_ru = request.POST.get("i_ru")
            gmipimsstatic.rues = request.POST.get("rues")
            gmipimsstatic.ne = request.POST.get("ne")
            gmipimsstatic.descript = request.POST.get("descript")
            gmipimsstatic.ip = request.POST.get("ip")
            gmipimsstatic.mask = request.POST.get("mask")
            gmipimsstatic.gw = request.POST.get("gw")
            gmipimsstatic.ip_in = request.POST.get("ip_in")
            gmipimsstatic.port_in = request.POST.get("port_in")
            gmipimsstatic.hard = request.POST.get("hard")
            gmipimsstatic.sn = request.POST.get("sn")
            gmipimsstatic.prim1 = request.POST.get("prim1")
            gmipimsstatic.save()
            return HttpResponseRedirect("/gm_ipadr/"+gmipimsstatic.i_ru+"/")
        else:
            return render(request, "edit_gm_ipadr.html", {"gmipimsstatic": gmipimsstatic})
    except Gmipimsstatic.DoesNotExist:
        return HttpResponseNotFound("<h2>Gmipimsstatic not found</h2>")
     
# удаление данных из бд
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.i_ru = request.POST.get("i_ru")
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
