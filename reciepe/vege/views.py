from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def receipes(request):
    print("request",request.method)
    if request.method == "POST":
        data= request.POST
        # print("data",data)
        file = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        # print(file,"file")
        
        Receipe.objects.create(receipe_name=receipe_name,receipe_description=receipe_description,receipe_image=file)
        
        return redirect('/receipes')

    queryset = Receipe.objects.all()
    queryset.delete()
    
    if request.GET.get('search'):
        # print("search vale",request.GET.get('search'))
        queryset = queryset.filter(receipe_name__icontains=request.GET.get('search'))
    # else:
        
    print("queryset",queryset)
    context = {'receipes':queryset}
    return render(request, 'receipes.html',context)

def delete_receipe(request,id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipes')

def update_receipe(request,id):
    queryset = Receipe.objects.get(id=id)
    context = {'receipe':queryset}
    if request.method == "POST":
        data= request.POST
        print("data",data)
        file = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        
        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        
        if file:
            queryset.receipe_image = file  
        queryset.save()
        return redirect('/receipes')     
    
    return render(request, 'update_receipe.html', context)