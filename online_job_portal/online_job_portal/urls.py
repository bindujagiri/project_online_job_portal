"""
URL configuration for online_job_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from job.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name="index"),
    path('admin_login', admin_login,name="admin_login"),
    path('user_login', user_login,name="user_login"),
    path('recruiter_login', recruiter_login,name="recruiter_login"),
    path('user_sign_up', user_sign_up,name="user_sign_up"),
    path('user_home', user_home,name="user_home"),
    path('Logout', Logout,name="Logout"),
    path('recruiter_signup', recruiter_signup,name="recruiter_signup"),
    path('recruiter_home', recruiter_home,name="recruiter_home"),
    path('admin_home', admin_home,name="admin_home"),
    path('view_users', view_users,name="view_users"),
    path('pending', pending,name="pending"),
    path('delete_user//<int:pid>', delete_user,name="delete_user"),
    path('change_status//<int:pid>',change_status,name="change_status"),
    path('recruiter_accepted',recruiter_accepted,name="recruiter_accepted"),
    path('recruiter_rejected',recruiter_rejected,name="recruiter_rejected"),
    path('recruiters_all',recruiters_all,name="recruiters_all"),
    path('delete_recruiter//<int:pid>', delete_recruiter,name="delete_recruiter"),
    path('change_password_admin',change_password_admin,name="change_password_admin"),
    path('change_password_user',change_password_user,name="change_password_user"),
    path('change_password_recruiter',change_password_recruiter,name="change_password_recruiter"),
    path('add_job', add_job,name="add_job"),
    path('job_list', job_list,name="job_list"),
    path('edit_job_recruiter//<int:pid>', edit_job_recruiter,name="edit_job_recruiter"),
    path('latest_jobs', latest_jobs,name="latest_jobs"),
    path('change_companylogo//<int:pid>', change_companylogo,name="change_companylogo"),
    path('user_latestjobs', user_latestjobs,name="user_latestjobs"),
    path('job_details//<int:pid>', job_details,name="job_details"),
    path('applyforjob//<int:pid>', applyforjob,name="applyforjob"),
    path('applied_candidatelist', applied_candidatelist,name="applied_candidatelist"),
    path('contact_us', contact_us,name="contact_us"),
    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


