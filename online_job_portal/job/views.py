from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date

# Create your views here.
def index(request):
    return render(request,'index.html')

def admin_login(request):
     error =""
     if request.method == "POST" :
             u = request.POST['uname']
             p = request.POST['pwd']
             user = authenticate(username=u,password=p)
       
             try:
                    if user.is_staff:
                     login(request,user)
                     error ="no"

                    else:
                        error ="yes"  
             except:  
                error = "yes"  
     else:
                error = "yes"  

     d = {'error': error}             
     return render(request,'admin_login.html',d)


def admin_home(request):
    if not  request.user.is_authenticated:
          return redirect('admin_login')
    
    rcount=Recruiter.objects.all().count()
    scount=StudentUser.objects.all().count()
    d={'rcount':rcount,'scount':scount}

    return render(request,'admin_home.html',d)

def user_login(request):
    error =""
    if request.method == "POST" :
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username = u ,password = p)
        if user:
            try:

                user1 = StudentUser.objects.get(user=user)
                if user1.type == "student":
                    login(request,user)
                    error ="no"

                else:
                    error ="yes"    

            except:  
                error = "yes"  
        else:
            error = "yes"  

    d = {'error': error}   

    return render(request,'user_login.html',d)
    


def recruiter_login(request):


    error =""
    if request.method == "POST" :
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username = u ,password = p)
        if user:
            try:

                user1 = Recruiter.objects.get(user=user)
                if user1.type == "recruiter" and user1.status != "pending":
                    login(request,user)
                    error ="no"

                else:
                    error ="not"    

            except:  
                error = "yes"  
        else:
            error = "yes"  

    d = {'error': error}   

    return render(request,'recruiter_login.html',d)



def recruiter_signup(request):
   

    error=" "
    if request.method=="POST":
        f=request.POST['fname']
        l=request.POST['lname']
        i=request.FILES['image'] 
        p=request.POST['pwd']
        e=request.POST['email']
        company=request.POST['company']
        country=request.POST['country']
        con=request.POST['contact']
        gen=request.POST['gender']
        
        
        

        try:
            user = User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
            Recruiter.objects.create(user=user,mobile=con,image=i,gender=gen,company=company,country=country,type="recruiter",status="pending")
            error="no"
        except:
            error="yes"    
            
    d = {'error': error}
    return render(request,'recruiter_signup.html',d)


def recruiter_home(request):

    if not  request.user.is_authenticated:
         return redirect('recruiter_login')
    user = request.user
    recruiter= Recruiter.objects.get(user=user)

    error=" "
    if request.method=="POST":
        f=request.POST['fname']
        l=request.POST['lname']
      
        con=request.POST['contact']
        gen=request.POST['gender']
        
        recruiter.user.first_name= f
        recruiter.user.last_name= l
       
        recruiter.mobile= con
        recruiter.gender= gen

        try:
            recruiter.save()
            error="no"
        except:
            error="yes" 

        try:
            i=request.FILES['image']
            recruiter.image=i
            recruiter.save()
            recruiter.user.save()
            error="no"
        except:
            pass  

    d={'recruiter':recruiter,'error':error}
    return render(request,'recruiter_home.html',d)



def user_home(request):

    if not  request.user.is_authenticated:
         return redirect('user_login')
    user = request.user
    student= StudentUser.objects.get(user=user)

    error=" "
    if request.method=="POST":
        f=request.POST['fname']
        l=request.POST['lname']
      
        con=request.POST['contact']
        gen=request.POST['gender']
        
        student.user.first_name= f
        student.user.last_name= l
       
        student.mobile= con
        student.gender= gen

        try:
            student.save()
            error="no"
        except:
            error="yes" 

        try:
            i=request.FILES['image']
            student.image=i
            student.save()
            student.user.save()
            error="no"
        except:
            pass  

    d={'student':student,'error':error}
    
    return render(request,'user_home.html',d)


def Logout(request):
    logout(request)
    return redirect('index')

def user_sign_up(request):
    error=" "
    if request.method=="POST":
        f=request.POST['fname']
        l=request.POST['lname']
        i=request.FILES['image']
        p=request.POST['pwd']
        e=request.POST['email']
        con=request.POST['contact']
        gen=request.POST['gender']
        

        try:
            user = User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
            StudentUser.objects.create(user=user,mobile=con,image=i,gender=gen,type="student")
            error="no"
        except:
            error="yes"    
            
    d = {'error': error}
    return render(request,'user_sign_up.html',d)


def view_users(request):
    if not  request.user.is_authenticated:
         return redirect('admin_login')
    data = StudentUser.objects.all()
    d={'data':data}
    return render(request,'view_users.html',d)


def pending(request):
    if not  request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status='pending')
    d={'data':data}
    return render(request,'pending.html',d)

def delete_user(request,pid):
    if not  request.user.is_authenticated:
         return redirect('admin_login')
    student = User.objects.get(id=pid)
    student.delete()
    return redirect('view_users')


def recruiter_accepted(request):
    if not  request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status='Accept')
    d={'data':data}
    return render(request,'recruiter_accepted.html',d)

def recruiter_rejected(request):
    if not  request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status='Reject')
    d={'data':data}
    return render(request,'recruiter_rejected.html',d)


def recruiters_all(request):
    if not  request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.all()
    d={'data':data}
    return render(request,'recruiters_all.html',d)




def change_status(request,pid):
    if not  request.user.is_authenticated:
        return redirect('admin_login')
    error=""
    recruiter = Recruiter.objects.get(id=pid)
    if request.method=="POST":
        s=request.POST['status']
        recruiter.status=s
        try:
            recruiter.save()
            error="no"
        except:
            error="yes"    
    d={'recruiter':recruiter,'error':error}
    return render(request,'change_status.html',d)

def delete_recruiter(request,pid):
    if not  request.user.is_authenticated:
         return redirect('admin_login')
    recruiter = User.objects.get(id=pid)
    recruiter.delete()
    return redirect('recruiters_all')


def change_password_admin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=""
    
    if request.method=="POST":
        c=request.POST['currentpassword']
        n=request.POST['newpassword']
       
        try:
            u=User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"


        except:
            error="yes"    
    d = {'error':error}
    return render(request,'change_password_admin.html',d)


def change_password_user(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error=""
    
    if request.method=="POST":
        c=request.POST['currentpassword']
        n=request.POST['newpassword']
       
        try:
            u=User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"


        except:
            error="yes"    
    d = {'error':error}
    return render(request,'change_password_user.html',d)




def change_password_recruiter(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error=""
    
    if request.method=="POST":
        c=request.POST['currentpassword']
        n=request.POST['newpassword']
       
        try:
            u=User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"


        except:
            error="yes"    
    d = {'error':error}
    return render(request,'change_password_recruiter.html',d)


def add_job(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error=" "
    if request.method=="POST":
        jt=request.POST['jobtitle']
        sd=request.POST['startdate']
        ed=request.POST['enddate']
        sal=request.POST['salary']
        logo=request.FILES['logo']
        exp=request.POST['experience']
        loc=request.POST['location']
        skills=request.POST['skills']
        des=request.POST['description']
        user= request.user
        recruiter=Recruiter.objects.get(user=user)

        try:
            Job.objects.create(recruiter=recruiter,start_date=sd,end_date=ed,title=jt,salary=sal,image=logo,experience=exp,description=des,location=loc,skills=skills,creationdate=date.today())
            error="no"
        except:
            error="yes"    
            
    d = {'error': error}
    
    
    return render(request,'add_job.html',d)


def job_list(request):
    if not  request.user.is_authenticated:
        return redirect('recruiter_login')
    user = request.user
    recruiter=Recruiter.objects.get(user=user)
    job = Job.objects.filter(recruiter=recruiter)

    d={'job':job}
    return render(request,'job_list.html',d)


def edit_job_recruiter(request,pid):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error=" "
    job=Job.objects.get(id=pid)
    if request.method=="POST":
        jt=request.POST['jobtitle']
        sd=request.POST['startdate']
        ed=request.POST['enddate']
        sal=request.POST['salary']
        exp=request.POST['experience']
        loc=request.POST['location']
        skills=request.POST['skills']
        des=request.POST['description']
       
        job.title=jt
        job.salary=sal
        job.experience=exp
        job.location=loc
        job.skills=skills
        job.description=des
        try:
            job.save()
            error="no"
        except:
            error="yes" 
        if sd:
            try:
                job.start_date=sd
                job.save()


            except:  
                pass

        else:
            pass 

        if sd:
            try:
                job.end_date=ed
                job.save()


            except:  
                pass

        else:
            pass              


    d = {'error': error,'job':job}    
    return render(request,'edit_job_recruiter.html',d)


def change_companylogo(request,pid):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error=" "
    job=Job.objects.get(id=pid)
    if request.method=="POST":
        cl=request.FILES['logo']
        job.image=cl
        
        try:
            job.save()
            error="no"
        except:
            error="yes" 
       

    d = {'error': error,'job':job}    
    return render(request,'change_companylogo.html',d)

def latest_jobs(request):
    
    job = Job.objects.all().order_by('-start_date')
    d={'job':job}
    return render(request,'latest_jobs.html',d)



def user_latestjobs(request):
    
    job = Job.objects.all().order_by('-start_date')
    user=request.user
    student= StudentUser.objects.get(user=user)
    data=Apply.objects.filter(student=student)
    li=[]
    for i in data:
        li.append(i.job.id)

    d={'job':job,'li':li}

    return render(request,'user_latestjobs.html',d)



def job_details(request,pid):
    
    job = Job.objects.get(id=pid)
    d={'job':job}
    return render(request,'job_details.html',d)



def applyforjob(request,pid):
    
    if not request.user.is_authenticated:
        return redirect('user_login')
    error=""
    user=request.user
    student=StudentUser.objects.get(user=user)
    job=Job.objects.get(id=pid)
    date1=date.today()
    if job.end_date < date1:
        error="close"
        
    elif job.start_date > date1:
        error="notopen"

    else:    
        if request.method=="POST":
            r=request.FILES['resume']
            Apply.objects.create(job=job,student=student,resume=r,apply_date=date.today())
            error="done"
            
        
        try:
            job.save()
            error="no"
        except:
            error="yes" 
       

    d = {'error': error,'job':job}  
    return render(request,'applyforjob.html',d)

def applied_candidatelist(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    
    data=Apply.objects.all()
       

    d = {'data': data}    
    return render(request,'applied_candidatelist.html',d)



def contact_us(request):
    return render(request,'contact_us.html')