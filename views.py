from django.shortcuts import render
from .forms import employeeregi
from .models import Emp
from django.http import HttpResponseRedirect
# Create your views here.

# This function is use for add and show data
def empdata(request):
    if request.method == 'POST':
        fm = employeeregi(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            alldata = Emp(name=nm,email=em,password=pw)
            alldata.save()
            fm = employeeregi()
    else:        
       fm = employeeregi()
    data = Emp.objects.all()
    return render(request,'myapp/addemp.html',{'form':fm,'data':data})

# This function is use for delete
def delete_data(request,id):
    if request.method == 'POST':
        dl = Emp.objects.get(pk=id)
        dl.delete()
        return HttpResponseRedirect('/')

# This function is use for Edit & Update 
def edit_data(request,id):
    if request.method == 'POST':
        ed = Emp.objects.get(pk=id)
        fm = employeeregi(request.POST,instance=ed)
        if fm.is_valid():
            fm.save()
    else:
        ed = Emp.objects.get(pk=id)
        fm = employeeregi(instance=ed)    
    return render(request,'myapp/edit.html',{'form':fm})    

               
