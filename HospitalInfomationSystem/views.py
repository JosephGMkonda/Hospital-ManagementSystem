from django.shortcuts import render
from HospitalInfomationSystem.EmailService import EmailService
from django.contrib.auth import login,logout as auth_logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages




def loginView(request):
    return render (request, 'login.html')

def LoginFunctionView(request):

    if request.method != "POST":
        return HttpResponse("<h2>Method is not allowed</h2>")
    else:
        user = EmailService.emailAuthentication(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user != None:
            login(request,user)
            if user.user == "1":
                return HttpResponseRedirect("/admin_home")
            elif user.user == "2":
                return HttpResponseRedirect("/doctor_home")
            else:
                return HttpResponseRedirect("/nurse_home")

        else:
            messages.error(request,'Invalid Login details')
            return HttpResponseRedirect("/")
        

def userDatails(request):
    if request.user != None:
        return HttpResponse("User : "+request.user.email + " user: "+str(request.user.user))

    else:
        return HttpResponse("please login first")
            
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect("/")

                
