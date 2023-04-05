from django.urls import path, re_path

from . import Administrator,Doctor
from . import views

urlpatterns = [
#    Auth URLs
    path('',views.loginView, name='showlogin'),
    path('login',views.LoginFunctionView,name='login'),
    path('logout', views.logout, name="logout"),

# Adding  and Managing Doctors URLs
    path('admin_home',Administrator.admin_home, name="admin_home"),
    path('add_doctor',Administrator.add_doctor,name='add_doctor'),
    path('save_doctor',Administrator.save_doctor, name="save_doctor"),
    path('manage_doctor',Administrator.manage_doctor, name="manage_doctor"),
    path('edit_doctor/<str:doctor_id>', Administrator.edit_doctor,name='edit_doctor'),
    path('edit_doctor_save',Administrator.edit_doctor_save,name="edit_doctor_save"),

# Adding and Managing Nurses URLs
   path('add_nurse',Administrator.add_nurse,name='add_nurse'),
   path('manage_nurse',Administrator.manage_nurse, name="manage_nurse"),
   path('save_nurse',Administrator.save_nurse, name="save_nurse"),



# Doctor URLs

path('doctor_home',Doctor.doctor_home, name="doctor_home"),
path('add_outPetient',Doctor.add_outPetient, name="add_outPetient"),
path('save_OutPetient',Doctor.save_OutPetient, name="save_OutPetient"),
path('manage_OutPetient',Doctor.manage_OutPetient, name="manage_OutPetient"),
path('add_admision',Doctor.add_addmision, name="add_admision"),
path('save_admision',Doctor.save_admision, name="save_admision"),
path('manage_admision',Doctor.manage_admision, name="manage_admision"),
path('edit_admision/<int:id>',Doctor.edit_admision, name="edit_admision"),
path('delete_admission/<int:id>',Doctor.delete_admission,name="delete_admission"),



]