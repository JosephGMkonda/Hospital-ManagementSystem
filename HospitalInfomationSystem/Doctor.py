from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .models import OutPatient,AdmittedPatient
from django.contrib import messages


def doctor_home(request):
    return render(request,'Doctor/doctor_home.html')


def add_outPetient(request):
    return render(request, 'Doctor/add_OutPetient.html')

def save_OutPetient(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method is not Allowed </h2>")
    else:
        fullname = request.POST.get("fullname")
        gender = request.POST.get("gender")
        village = request.POST.get("village")
        Disease = request.POST.get("Disease")
        visited_date = request.POST.get("visited_date")
        drug = request.POST.get("drug")

        try:
            petient = OutPatient.objects.create(FullName=fullname,Gender=gender,Village=village,diseases=Disease,visited=visited_date,drugs=drug)
            
            petient.save()
            
            print(petient.FullName)            
            messages.success(request,"Added Successfully")
            return HttpResponseRedirect("/manage_OutPetient")
            
        except:
            messages.error(request,"Process Failed")
            return HttpResponseRedirect("/add_OutPetient")
        
def manage_OutPetient(request):
    petient = OutPatient.objects.all()
    return render(request,'Doctor/manage_petient.html',{"petient":petient})



def add_addmision(request):
    return render(request,"Doctor/add_admision.html")

def save_admision(request):
    if request.method != "POST":
        return render("<h2>Method is Not Allowed </h2>")
    else:
        fullname = request.POST.get("fullname")
        gender = request.POST.get("gender")
        village = request.POST.get("village")
        Disease = request.POST.get("Disease")
        visited_date = request.POST.get("visited_date")
        ward_number = request.POST.get("ward_number")
        drug = request.POST.get("drug")
        
        try:
            admitted = AdmittedPatient.objects.create(Fullname = fullname,Gender=gender,village=village,diseases=Disease,admitted=visited_date,Bed_Number=ward_number,drugs=drug)
            admitted.save()
            messages.success(request,"added successfully")
            return HttpResponseRedirect("/manage_admision")
        except:
            messages.error(request,"process failed")
            return HttpResponseRedirect("/add_admision")
def manage_admision(request):
    admmited = AdmittedPatient.objects.all()
    return render(request, "Doctor/manage_admission.html",{"admmited":admmited})


def edit_admision(request, id):
    admitted = AdmittedPatient.objects.get(id=id)
    return render(request,"Doctor/Edit_Admision.html",{"admitted":admitted,"id":id})




def delete_admission(request,id):
    admitted = AdmittedPatient.objects.get(pk=id)
    admitted.delete()
    messages.success(request,"Patient Removed")
    return HttpResponseRedirect("/manage_admision")

    
            


            



        
