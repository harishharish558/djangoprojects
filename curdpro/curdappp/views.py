from django.shortcuts import render
from .models import createmodel
from .forms import createform,updateform,deleteform
from django.http.response import HttpResponse

def homeview(request):
    return render(request,'home.html')
def createview(request):
    if request.method == 'POST':
        cform=createform(request.POST)
        if cform.is_valid():
            rollno=request.POST.get('studentnumber',' ')
            fname=request.POST.get('firstname',' ')
            lname=request.POST.get('lastname',' ')
            mobile=request.POST.get('mobile',' ')
            email=request.POST.get('email',' ')
            data=createmodel(
                studentnumber=rollno,
                firstname=fname,
                lastname=lname,
                mobile=mobile,
                email=email,
                          )
            data.save()
        cform = createform()
        return render(request, 'create.html', {'cform': cform})
    else:
        cform=createform()
        return render(request,'create.html',{'cform':cform})


def updateview(request):
    if request.method=='POST':
        uform=updateform(request.POST)
        if uform.is_valid():
            studentnumber=request.POST.get('studentnumber','')
            fname=request.POST.get('firstname',' ')
            lname=request.POST.get('lastname','')
            rollno=createmodel.objects.filter(studentnumber=studentnumber)
            if not rollno:
                return HttpResponse('<h1>Invalid student identity number details</h1>')
            else:
                rollno.update(firstname=fname,lastname=lname)
                uform=updateform()
                return render(request,'update.html',{'uform':uform})
    else:
        uform=updateform()
        return render(request,'update.html',{'uform':uform})


def retrieve_view(request):
    data=createmodel.objects.all()
    ldata=len(data)
    return render(request,'retrieve.html',{'data':data,'ldata':ldata})


def deleteview(request):
    if request.method=='POST':
        dform=deleteform(request.POST)
        if dform.is_valid():
            rollno=request.POST.get('studentnumber',' ')
            studentnumber=createmodel.objects.filter(studentnumber=rollno)
            if not studentnumber:
                return HttpResponse('<h1>Invalid student number</h1>')
            else:
                studentnumber.delete()
                dform = deleteform()
                return render(request, 'delete.html', {'dform': dform})

    else:
        dform=deleteform()
        return render(request,'delete.html',{'dform':dform})