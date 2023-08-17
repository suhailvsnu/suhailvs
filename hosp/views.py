from django.shortcuts import render,redirect
from hosp.models import tbl_doctor,tbl_nurse


# Create your views here.
def doctor(request):
    return render(request,'doctor.html')
def nurse(request):
    return render (request,'nurse.html')
def index(request):
    return render(request,'index.html')
def adddoctor(request):
    a=tbl_doctor()
    a.name=request.POST.get("name")
    a.age=request.POST.get("age")
    a.specilization=request.POST.get("spcl")
    a.experience=request.POST.get("exp")
    a.salary=request.POST.get("sal")
    a.save()

    return redirect('/doctor/')
def addnurse(request):
    b=tbl_nurse()
    b.name=request.POST.get("name")
    b.age=request.POST.get("age")
    b.qualification=request.POST.get("qual")
    b.experience=request.POST.get("exp")
    b.salary=request.POST.get("sal")
    b.save()
    return redirect('/nurse/')
def  viewdoctor(request):
    e=tbl_doctor.objects.all()
    return render(request,'doctorview.html',{'data':e})
def viewnurse(request):
    b=tbl_nurse.objects.all()
    return render(request,'nurseview.html',{'data':b})
def delnurse(request,id):
    d=tbl_nurse.objects.get(id=id)
    d.delete()
    return redirect('/viewnurse/')
def deldoc(request,id):
    s=tbl_doctor.objects.get(id=id)
    s.delete()
    return redirect('/doctorview/')
def updnurse1(request,id):
    a=tbl_nurse.objects.get(id=id)
    return render(request,'updatenurse.html',{'x':a})
def updnurse2(request,id):
    a=tbl_nurse.objects.get(id=id)
    a.name=request.POST.get('name')
    a.age=request.POST.get('age')
    a.qualification=request.POST.get('qal')
    a.experience=request.POST.get('exp')
    a.salary=request.POST.get('sal')
    
    a.save()
    return redirect('/viewnurse/')
def upddoc1(request,id):
    a=tbl_doctor.objects.get(id=id)
    return render(request,'updatedoctor.html',{'x':a})
def upddoc2(request,id):
    a=tbl_doctor.objects.get(id=id)
    a.name=request.POST.get('name')
    a.age=request.POST.get('age')
    a.specilization=request.POST.get('spl')
    a.experience=request.POST.get('exp')
    # a.salary=request.POST.get('sal')
    a.save()
    return redirect('/doctorview/')

