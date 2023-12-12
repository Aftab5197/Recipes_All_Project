from django.shortcuts import render, redirect

from recepieapp.models import *


# Create your views here.
def home(request):
    recepies=Recepie.objects.all()
    data={'recepie':recepies}
    return render(request,'home.html',data)


def add(request):
    if request.method=='POST':
        data=request.POST
        recepie_name=data.get('recepie_name')
        recepie_description = data.get('recepie_description')
        recepie_image = request.FILES.get('recepie_image')
        Recepie.objects.create(
            recepie_name=recepie_name,
            recepie_description=recepie_description,
            recepie_image=recepie_image,
        )
        return redirect(home)
    return render(request,'add.html')


def delete_recepie(request,id):
    queryset=Recepie.objects.get(id = id)
    queryset.delete()
    return redirect(home)





def update_recepie(request,id):
    queryset=Recepie.objects.get(id=id)
    if request.method=='POST':
        data=request.POST
        recepie_name=data.get('recepie_name')
        recepie_description = data.get('recepie_description')
        recepie_image = request.FILES.get('recepie_image')

        queryset.recepie_name = recepie_name
        queryset.recepie_description = recepie_description
        queryset.recepie_image = recepie_image
        queryset.save()
        return redirect(home)

    context={'recepie':queryset}
    return render(request,'edit.html',context)


def searchbar(request):
    if request.method=='GET':
        query=request.GET['search']
        if query:
            recepie=Recepie.objects.filter(recepie_name__icontains=query)
            return  render(request,'search.html',{'recepie':recepie})

        else:
            print('no information to show')
            return redirect(home)
            return render(request,'search.html',{})
    return None