from django.shortcuts import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse


class LoginCheckMiddleWare(MiddlewareMixin):
    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename=view_func.__module__
        user=request.user


        if user.is_authenticated:
            if user.user == "1":
                if modulename == "HospitalInfomationSystem.Administrator":
                    pass
                elif modulename == "HospitalInfomationSystem.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("admin_home"))
                
            elif user.user == "2":
                if modulename == "HospitalInfomationSystem.Doctor":
                    pass
                elif modulename == "HospitalInfomationSystem.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("doctor_home"))

            elif user.user == "3":
                if modulename == "HospitalInfomationSystem.Nurse":
                    pass
                elif modulename == "HospitalInfomationSystem.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("nurse_home"))
                

        else:
            if request.path == reverse("showlogin") or request.path == reverse("login"):
                pass
            else:
                return HttpResponseRedirect(reverse("showlogin"))
 
            