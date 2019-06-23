from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import *

# Create your views here.
#-------------
def inventory(request):
    inventory = Inventory.objects.all().order_by('id')
    return render(request, 'PanelsForGame/inventory.html', {'inventory': inventory})

def inventory_new(request):
    form = PostInventory()
    if (request.method == "POST"):
        form = PostInventory(request.POST)
        if form.is_valid():
            pi = form.save(commit=False)
            pi.personage.id = request.POST['personage']
            pi.gObject.id = request.POST['gObject']
            pi.use_count = request.POST['use_count']
            pi.location_gObject.id = request.POST['location_gObject']
            pi.save()
            return redirect('inventory')
    return render(request, 'PanelsForGame/inventory_new.html', {'form': form})

def inventory_detail(request, id):
    pi = get_object_or_404(Inventory, id=id)
    if request.method == "POST":
        form = PostInventory(request.POST, instance=pi)
        if form.is_valid():
            pi = form.save(commit=False)
            pi.personage.id = request.POST['personage']
            pi.gObject.id = request.POST['gObject']
            pi.use_count = request.POST['use_count']
            pi.location_gObject.id = request.POST['location_gObject']
            pi.save()
            return redirect('inventory')
    else:
        form = PostInventory(instance=pi)
    return render(request, 'PanelsForGame/inventory_new.html', {'form': form})

def inventory_delete(request, id):
    inventorydelete = get_object_or_404(Inventory, id=id)
    if request.method == "POST":
        inventorydelete.delete()
        return redirect('inventory')
    else:
        return render(request, 'PanelsForGame/inventory_delete.html', { 'inventorydelete': inventorydelete })

#-------------
def personagetransfer(request):
    personagetransfer = PersonageTransfer.objects.all().order_by('id')
    return render(request, 'PanelsForGame/personagetransfer.html', {'personagetransfer': personagetransfer})

def personagetransfer_new(request):
    form = PostPersonageTransfer()
    if (request.method == "POST"):
        form = PostPersonageTransfer(request.POST)
        if form.is_valid():
            ppt = form.save(commit=False)
            ppt.personage.id = request.POST['personage']
            ppt.locations.id = request.POST['locations']
            ppt.save()
            return redirect('personagetransfer')
    return render(request, 'PanelsForGame/personagetransfer_new.html', {'form': form})

def personagetransfer_detail(request, id):
    ppt = get_object_or_404(PersonageTransfer, id=id)
    if request.method == "POST":
        form = PostPersonageTransfer(request.POST, instance=ppt)
        if form.is_valid():
            ppt = form.save(commit=False)
            ppt.personage.id = request.POST['personage']
            ppt.locations.id = request.POST['locations']
            ppt.save()
            return redirect('personagetransfer')
    else:
        form = PostPersonageTransfer(instance=ppt)
    return render(request, 'PanelsForGame/personagetransfer_new.html', {'form': form})

def personagetransfer_delete(request, id):
    personagetransferdelete = get_object_or_404(PersonageTransfer, id=id)
    if request.method == "POST":
        personagetransferdelete.delete()
        return redirect('personagetransfer')
    else:
        return render(request, 'PanelsForGame/personagetransfer_delete.html', { 'personagetransferdelete': personagetransferdelete })

#-------------
def personage(request):
    personages = Personage.objects.all().order_by('id')
    return render(request, 'PanelsForGame/personage.html', {'personages': personages})

def personage_new(request):
    form = PostPersonageDetail()
    if (request.method == "POST"):
        form = PostPersonageDetail(request.POST)
        if form.is_valid():
            pd = form.save(commit=False)
            pd.user.id = request.POST['user']
            pd.nick_name = request.POST['nick_name']
            pd.fraction.id = request.POST['fraction']
            pd.kill_count = request.POST['kill_count']
            pd.user.password = request.POST['passwd']
            pd.save()
            return redirect('personage')
    else:
        form = PostPersonageDetail()
    return render(request, 'PanelsForGame/personage_new.html', {'form': form})

def personage_delete(request, id):
    personagedelete = get_object_or_404(Personage, id=id)
    if request.method == "POST":
        personagedelete.delete()
        return redirect('personage')
    else:
        return render(request, 'PanelsForGame/personage_delete.html', { 'personagedelete': personagedelete })

def personage_detail(request, id):
    pd = get_object_or_404(Personage, id=id)
    if request.method == "POST":
        form = PostPersonageDetail(request.POST, instance=pd)
        if form.is_valid():
            pd = form.save(commit=False)

            if request.POST['passwd']:
                eu = get_object_or_404(Profile, id=pd.user.id)
                e_user = PostProfile(request.POST, instance=eu)
                e_user.passwd = request.POST['passwd']
                e_user.save()

            pd.user.id = request.POST['user']
            pd.nick_name = request.POST['nick_name']
            pd.fraction.id = request.POST['fraction']
            pd.kill_count = request.POST['kill_count']

            pd.save()
            return redirect('personage')
    else:
        form = PostPersonageDetail(instance=pd)
    return render(request, 'PanelsForGame/personage_new.html', {'form': form })
