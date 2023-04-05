from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .models import CustomUser,Doctor,Nurse
from django.contrib import messages



def admin_home(request):
    return render(request,'Admin/Home.html')

def add_doctor(request):
    return render (request,'Admin/add_doctor.html')

def save_doctor(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method is not found</h2>")
    else:
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        gender = request.POST.get("gender")
        contact = request.POST.get("contact_number")


        try:
            user = CustomUser.objects.create_user(email=email,username=username,password=password,first_name=first_name,last_name=last_name,user=2)
            user.doctor.Gender = gender
            user.doctor.Contact_Number = contact
            user.save()
            messages.success(request,"Doctor Added Successfully")
            return HttpResponseRedirect("/manage_doctor")
        except:
            messages.error(request,"Failed to add Doctor")
            return HttpResponseRedirect("/add_doctor")
        
def manage_doctor(request):
    doctor = Doctor.objects.all()
    return render(request,"Admin/manage_doctor.html",{"doctor":doctor})

def edit_doctor(request, doctor_id):
    doctor = Doctor.objects.get(admin=doctor_id)
    return render(request, "Admin/edit_doctor.html",{"doctor":doctor, "id":doctor_id})

def edit_doctor_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method is not allowed</h2>")
    else:
        doctor_id = request.POST.get("doctor_id")
        email = request.POST.get("email")
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        contact_number= request.POST.get("contact_number")


        user = CustomUser.objects.get(id=doctor_id)
        print(user)
        user.email = email
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        doctor_model = Doctor.objects.get(admin=doctor_id)
        doctor_model.Contact_Number = contact_number
        doctor_model.save()
        messages.success(request, "Doctor is Updated SuccessFully")
        return HttpResponseRedirect("/manage_doctor"+doctor_id)
    
    
        messages.error(request,"Fail to update Doctor")
        return HttpResponseRedirect("/edit_doctor")

    
        

# managing nurses 

def add_nurse(request):
    return render (request,'Admin/add_nurse.html')

def save_nurse(request):
    if request.method != "POST":
        return HttpResponse("Method is not found")
    else:
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        gender = request.POST.get("gender")
        contact = request.POST.get("contact_number")

        user = CustomUser.objects.create_user(email=email,username=username,password=password,first_name=first_name,last_name=last_name,user=3)
        user.nurse.gender = gender
        user.nurse.contact = contact
        user.save()
        messages.success(request,"Doctor Added Successfully")
        return HttpResponseRedirect("/manage_nurse")
        
        messages.error(request,"Failed to add Nurse")
        return HttpResponseRedirect("/add_nurse")


    
         
        
def manage_nurse(request):
    nurse = Nurse.objects.all()
    return render(request,"Admin/manage_nurse.html",{"nurse":nurse})







    