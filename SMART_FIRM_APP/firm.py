from django.shortcuts import render
import mysql.connector
from mysql.connector import Error
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.core.files.storage import FileSystemStorage

def LandingPage(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def ReadMore(request):
    return render(request, 'ReadMore.html')

def EMPLeaveManagement(request):
    return render(request, 'EMPleave.html')

def MANLeaveManagement(request):
    return render(request, 'MANleave.html')

def registrationPage(request):
    conn = mysql.connector.connect(host='localhost', database='smart_firm', user='root', password='root',
                                   auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    query = "select * from department"
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)
    return render(request, 'EMPregistration.html',{'rows':rows})

def otherRegistrationPage(request):
    conn = mysql.connector.connect(host='localhost', database='smart_firm', user='root', password='root',
                                   auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    query = "select * from department"
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)
    return render(request, 'MANregistration.html',{'rows':rows})

def loginPage(request):
    return render(request, 'login.html')

def ConfCall(request):
    return render(request, 'ConferenceCall.html')

def dailyTask(request):
    conn = mysql.connector.connect(host='localhost', database='smart_firm', user='root', password='root',auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    query = "select * from department"
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)
    return render(request, 'EMPdailyTask.html',{'rows':rows})

def EMPReg(request):
    try:
        username=request.POST.get('Username')
        email=request.POST.get('Email')
        password = request.POST.get('Password')
        department = int(request.POST.get('Department'))
        city=request.POST.get('City')
        mo=request.POST.get('MO')
        gender=request.POST.get('gender')

        conn=mysql.connector.connect(host='localhost' , database='smart_firm', user='root', password='Admin',auth_plugin='mysql_native_password')
        cursor = conn.cursor()
        query="insert into login (username,password,role) VALUES ('%s','%s','%s')" %(email,password,'employee')
        cursor.execute(query)
        conn.commit()
        #msg="VALUE ADDED"
        id=cursor.lastrowid
        print("last row id is : ",id)
        query1="insert into emp_registration (name,city,mo,emp_lid,gender,e_d_id) VALUES ('%s','%s','%s','%d','%s','%d')" %(username,city,mo,id,gender,department)
        cursor.execute(query1)
        conn.commit()
        return HttpResponse("DATA ADDED....!")
            #render(request, 'EMPregistration.html',{'msg':msg})

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def MANReg(request):
    try:
        username=request.POST.get('Username')
        email=request.POST.get('Email')
        password = request.POST.get('Password')
        department = int(request.POST.get('Department'))
        city=request.POST.get('City')
        mo=request.POST.get('MO')
        gender=request.POST.get('gender')

        conn=mysql.connector.connect(host='localhost' , database='smart_firm', user='root', password='Admin',auth_plugin='mysql_native_password')
        cursor = conn.cursor()
        query="insert into login (username,password,role) VALUES ('%s','%s','%s')" %(email,password,'manager')
        cursor.execute(query)
        conn.commit()
        #msg="VALUE ADDED"
        id=cursor.lastrowid
        print("last row id is : ",id)
        query1="insert into man_registration (name,city,mo,man_lid,gender,m_d_id) VALUES ('%s','%s','%s','%d','%s','%d')" %(username,city,mo,id,gender,department)
        cursor.execute(query1)
        conn.commit()
        return HttpResponse("DATA ADDED....!")
            #render(request, 'MANregistration.html',{'msg':msg})

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def AppLogin(request):
    try:
        email=request.POST.get('Email')
        password = request.POST.get('Password')

        conn=mysql.connector.connect(host='localhost' , database='smart_firm', user='root', password='root',auth_plugin='mysql_native_password')
        cursor = conn.cursor()
        query="select lid,role from login WHERE username='%s' AND password='%s'" %(email,password)
        cursor.execute(query)
        rows=cursor.fetchone()
        print("data is : ",rows)
        if rows:
            role=rows[1]
            lid=rows[0]
            request.session['lid']=lid
            #msg="user id "+lid
            if (role=='admin'):
                return render(request, 'admin.html')
                #return HttpResponse("HELLO ADMIN....!")

            elif (role=='employee'):
                return render(request, 'employee.html')
                #return HttpResponse("HELLO EMPLOYEE....!")
            else:
                return render(request,'manager.html')
                #return HttpResponse("HELLO manager....!")

        else:
            return HttpResponse("PLEASE ENTER VALID INFORMATION....!")


    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def forgotPass(request):
    try:
        email = EmailMessage('password','78945612',to=['deep041999@gmail.com'])
        email.send()

    except:
        print("hello your password is")

    return HttpResponse("mail send...!")

def EMPworkingWeekend(request):
    return render(request, 'EMPWorkingWeekend.html')

def EMP_daily_task(request):
    try:
        taskname=request.POST.get('Taskname')
        projectname=request.POST.get('Projectname')
        department = int(request.POST.get('eDepartment'))
        desc = request.POST.get('Description')
        emp_id = request.session.get('lid')

        conn=mysql.connector.connect(host='localhost' , database='smart_firm', user='root', password='root',auth_plugin='mysql_native_password')
        cursor = conn.cursor()
        query1="select emp_rid from emp_registration WHERE emp_lid='%d'" %(emp_id)
        cursor.execute(query1)
        dt_e=cursor.fetchone()
        dt=dt_e[0]
        query="insert into emp_daily_task (task_name,project_name,dt_d_id,description,dt_emp_id) VALUES ('%s','%s','%d','%s','%d')" %(taskname,projectname,department,desc,dt)
        cursor.execute(query)
        conn.commit()
        #msg="VALUE ADDED"
        return HttpResponse("DATA ADDED....!")
        #render(request, 'MANregistration.html',{'msg':msg})

    except Error as e:
        print(e)

    finally:
        # cursor.close()
        conn.close()

def MAN_daily_task(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='smart_firm', user='root', password='root',
                                       auth_plugin = 'mysql_native_password')
        cursor = conn.cursor()
        query = "select * FROM emp_daily_task where status='Pending'"
        cursor.execute(query)
        row2 = cursor.fetchall()
        print(row2)
        return render(request, 'MANdailyTask.html',{'row2':row2})

    except Error as e:
        print(e)


    finally:
        cursor.close()
        conn.close()

def DtACCEPT(request):

     try:
         id = int(request.GET.get('emp_id'))
         man_id = request.session.get('lid')
         #id= int(request.GET.get('id'))
         conn = mysql.connector.connect(host='localhost', database='smart_firm', user='root', password='root',
                                        auth_plugin = 'mysql_native_password')
         cursor = conn.cursor()

         query2 = "select man_rid from man_registration WHERE man_lid='%d'" % (man_id)
         cursor.execute(query2)
         dt_m = cursor.fetchone()
         mid = dt_m[0]

         query = "update emp_daily_task SET status = 'Accepted', man_id = '%d' where emp_dt_id='%d'" %(mid,id)
         cursor.execute(query)
         #query2 = #"update emp_daily_task SET man_id = '%d' where emp_dt_id='%d'" % (man_rid,id)
         #cursor.execute(query2)

         query1 = "select l.username from login as l join emp_registration as er on er.emp_lid = l.lid join emp_daily_task as edt on edt.dt_emp_id = er.emp_rid where edt.emp_dt_id = %d" %(id)
         cursor.execute(query1)
         emailid = cursor.fetchone()
         print(emailid[0])
         conn.commit()

         subject = "SMART FIRM DAILY TASK ACCEPTED MAIL"
         body = "your request for daily task is ACCEPTED by DEEP PATEL...!!!!"
         email   = EmailMessage(subject, body, to=[emailid[0]])
         print(email)

         email.send()
         print('done')

         #return MAN_daily_task(request)
         return render(request, 'DailyTaskEmpFeedback.html',{'id':id})

     except Error as e:
         print(e)

     finally:
        cursor.close()
        conn.close()

def DtREJECT(request):

     try:
         id = int(request.GET.get('emp_id'))
         #lid = request.session.get('lid')
         man_id = request.session.get('lid')
         #id= int(request.GET.get('id'))
         conn = mysql.connector.connect(host='localhost', database='smart_firm', user='root', password='root',
                                        auth_plugin = 'mysql_native_password')
         cursor = conn.cursor()

         query2 = "select man_rid from man_registration WHERE man_lid='%d'" % (man_id)
         cursor.execute(query2)
         dt_m = cursor.fetchone()
         mid = dt_m[0]

         query = "update emp_daily_task SET status = 'Rejected', man_id = '%d' where emp_dt_id='%d'" % (mid, id)
         cursor.execute(query)

         query1 = "select l.username from login as l join emp_registration as er on er.emp_lid = l.lid join emp_daily_task as edt on edt.dt_emp_id = er.emp_rid where edt.emp_dt_id = %d" %(id)
         cursor.execute(query1)
         emailid = cursor.fetchone()
         print(emailid[0])
         conn.commit()

         subject = "SMART FIRM APPLICATION DT REJECTION MAIL"
         body = "your request for daily task is REJECTED by DEEP PATEL...!!!!"
         email   = EmailMessage(subject, body, to=[emailid[0]])
         email.send()
         print('done')

         conn.commit()
         return render(request, 'DailyTaskEmpFeedback.html', {'id': id})

     except Error as e:
         print(e)

     finally:
        cursor.close()
        conn.close()

def FeedbackDt(request):
    try:
        DtId=int(request.POST.get('dtid'))
        Feedback=request.POST.get('Feedback')
        Remarks=request.POST.get('Remarks')

        conn=mysql.connector.connect(host='localhost' , database='smart_firm', user='root', password='root',auth_plugin='mysql_native_password')
        cursor = conn.cursor()

        query2 = "select emp_dt_id,man_id from emp_daily_task WHERE emp_dt_id ='%d'" % (DtId)
        cursor.execute(query2)
        dt_f = cursor.fetchone()
        dt_id = dt_f[0]
        m_id=dt_f[1]

        query="insert into feedback_daily_task (DailyTaskId,ManagerId,Feedback,Remarks) VALUES ('%d','%d','%s','%s')" %(dt_id,m_id,Feedback,Remarks)
        cursor.execute(query)
        conn.commit()
        #msg="VALUE ADDED"
        return HttpResponse("DATA ADDED....!")
        #render(request, 'MANregistration.html',{'msg':msg})

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def ShowFeedback(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='smart_firm', user='root', password='root',
                                       auth_plugin='mysql_native_password')
        cursor = conn.cursor()

        query = "SELECT f.FeedbackID,f.DailyTaskId,dt.task_name,e.name AS Employee,m.name AS Manager,f.Feedback,f.Remarks,f.Date,dt.status " \
                 "FROM smart_firm.feedback_daily_task f INNER JOIN smart_firm.emp_daily_task dt " \
                    "ON f.DailyTaskId=dt.emp_dt_id INNER JOIN smart_firm.man_registration m " \
                    "ON dt.man_id=m.man_rid INNER JOIN smart_firm.emp_registration e " \
                    "ON dt.dt_emp_id=e.emp_rid;"
        cursor.execute(query)
        data=cursor.fetchall()

        return render(request, 'ShowFeedback.html', {'data': data})

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def EMPleave(request):

    try:
        conn = mysql.connector.connect(host='localhost', database='smart_firm', user='root', password='root',
                                          auth_plugin = 'mysql_native_password')
        cursor = conn.cursor()

        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            name = request.POST.get('Name')
            emp_lid = request.session.get('lid')

            query = "select emp_rid FROM emp_registration WHERE emp_lid='%d'" %(emp_lid)
            cursor.execute(query)

            row1 = cursor.fetchone()
            print(row1)
            r=row1[0]

            fs = FileSystemStorage()
            filename= myfile.name
            print("Filename=====", filename)
            extension = filename.split('.')
            print("Extension=====", extension)
            uploaded_file_name = name + "." +extension[1]

            filename = fs.save(uploaded_file_name, myfile)
            print("uploaded_file_name", filename)

            uploaded_file_url = fs.url(filename)
            print("uploaded_file_url", uploaded_file_url)
            #conn.commit()
            #return HttpResponse("Uploaded..!")

            #reason = request.POST.get('Reason')
            s_date = request.POST.get('StartDate')
            e_date = request.POST.get('EndDate')
            description = request.POST.get('Description')

            query1 = " insert into emp_leave (reason, start_date, end_date, description, file, emp_id, status) VALUES('%s','%s','%s','%s','%s','%d','%s') " % (name,s_date,e_date,description,uploaded_file_url,r,'pending')
            cursor.execute(query1)
            conn.commit()

            return HttpResponse("data is added")
            #return render(request, 'EMPleave.html')

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def MANleave(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='smart_firm', user='root', password='root',
                                       auth_plugin = 'mysql_native_password')
        cursor = conn.cursor()
        query = "select el.leave_id,el.reason,el.start_date,el.end_date,el.description,el.file,er.name FROM emp_leave as el left join emp_registration as er on el.emp_id = er.emp_rid where el.status='pending'"
        cursor.execute(query)
        row2 = cursor.fetchall()
        print(row2)
        return render(request, 'MANleave.html',{'row2':row2})

    except Error as e:
        print(e)


    finally:
        cursor.close()
        conn.close()

def ACCEPTuser(request):

     try:
         id = int(request.GET.get('emp_id'))
         #id= int(request.GET.get('id'))
         conn = mysql.connector.connect(host='localhost', database='smart_firm', user='root', password='root',
                                        auth_plugin = 'mysql_native_password')
         cursor = conn.cursor()
         query = "update emp_leave SET status = 'ACCEPTED' where leave_id='%d'" %(id)
         cursor.execute(query)

         query1 = "select l.username from login as l join emp_registration as er on er.emp_lid = l.lid join emp_leave as el on el.emp_id = er.emp_rid where el.leave_id = %d" %(id)
         cursor.execute(query1)
         emailid = cursor.fetchone()
         print(emailid[0])
         conn.commit()

         subject = "SMART FIRM APPLICATION LEAVE ACCEPTED MAIL"
         body = "your request for leave is ACCEPTED by DEEP PATEL...!!!!"
         email   = EmailMessage(subject, body, to=[emailid[0]])
         email.send()
         print('done')

         return MANleave(request)

     except Error as e:
         print(e)

     finally:
        cursor.close()
        conn.close()

def REJECTuser(request):

     try:
         id = int(request.GET.get('emp_id'))
         #id= int(request.GET.get('id'))
         conn = mysql.connector.connect(host='localhost', database='smart_firm', user='root', password='root',
                                        auth_plugin = 'mysql_native_password')
         cursor = conn.cursor()
         query = "update emp_leave SET status = 'REJECTED' where leave_id='%d'" %(id)
         cursor.execute(query)

         query1 = "select l.username from login as l join emp_registration as er on er.emp_lid = l.lid join emp_leave as el on el.emp_id = er.emp_rid where el.leave_id = %d" %(id)
         cursor.execute(query1)
         emailid = cursor.fetchone()
         print(emailid[0])
         conn.commit()

         subject = "SMART FIRM APPLICATION LEAVE REJECTION MAIL"
         body = "your request for leave is REJECTED by DEEP PATEL...!!!!"
         email   = EmailMessage(subject, body, to=[emailid[0]])
         email.send()
         print('done')

         conn.commit()
         return MANleave(request)

     except Error as e:
         print(e)

     finally:
        cursor.close()
        conn.close()

def emp_W_W(request):
    try:
        projectname = request.POST.get('PROJECT_NAME')
        emprole = request.POST.get('ROLE_OF_EMPLOYEE')
        wdate = request.POST.get('WEEKEND_DATE')
        conn = mysql.connector.connect(host='localhost', database='smart_firm', user='root', password='root',auth_plugin='mysql_native_password')
        cursor = conn.cursor()
        lid = request.session.get('lid')
        query1 = "select emp_rid FROM emp_registration WHERE emp_lid='%d'" %(lid)
        cursor.execute(query1)
        emp = cursor.fetchone()
        e=emp[0]
        print(emp)
        query = "insert into emp_w_w(eid ,PROJECT_NAME,ROLE_OF_EMPLOYEE,WEEKEND_DATE,STATUS) VALUES ('%d','%s','%s','%s','%s')" %(e ,projectname,emprole,wdate,'pending')
        print(query)
        cursor.execute(query)
        conn.commit()
        return HttpResponse("WEEKEND DATA ADDED....!")

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def MANworkingWeekend(request):
    conn = mysql.connector.connect(host='localhost', database='smart_firm', user='root', password='root',
                                   auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    query = "select  ew.PROJECT_NAME, ew.ROLE_OF_EMPLOYEE, ew.WEEKEND_DATE, ew.STATUS, er.name,ew.wid from emp_w_w as ew left " \
            "join emp_registration as er on ew.eid = er.emp_rid where ew.STATUS = 'pending'"
    cursor.execute(query)
    rows = cursor.fetchall()
    print("data is : ", rows)
    return render(request, 'MANWorkingWeekend.html', {'rows': rows})

def ACCEPT(request):
    try:
        id = int(request.GET.get('id'))
        conn = mysql.connector.connect(host='localhost', database='smart_firm', user='root', password='root',auth_plugin='mysql_native_password')
        cursor = conn.cursor()
        query = "update emp_W_W set status = 'accepted' where wid='%d'" %(id)
        print(query)
        cursor.execute(query)
        conn.commit()

        qry = "select l.username from login as l join emp_registration on emp_registration.emp_lid = l.lid join emp_w_w on emp_registration.emp_rid = emp_w_w.eid where emp_w_w.wid = %d" % id
        cursor.execute(qry)
        emailid = cursor.fetchone()
        print(emailid[0])
        conn.commit()
        subject = "SmartFirm Application Acception Mail"
        body = "Your application has been Accepted..!!"
        email = EmailMessage(subject, body, to=[emailid[0]])
        email.send()
        print('done')
        return MANworkingWeekend(request)
        #return MANworkingWeekend(request)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

    # return render(request, 'ACCEPTPAGE.html')

def REJECT(request):
    try:
        id = int(request.GET.get('id'))
        conn = mysql.connector.connect(host='localhost', database='smart_firm', user='root', password='root',
                                       auth_plugin='mysql_native_password')
        cursor = conn.cursor()
        query = "update emp_W_W set status = 'rejected' where wid='%d'" % (id)
        print(query)
        cursor.execute(query)

        qry = "select l.username from login as l join emp_registration on emp_registration.emp_lid = l.lid join emp_w_w on emp_registration.emp_rid = emp_w_w.eid where emp_w_w.wid = %d" %id
        cursor.execute(qry)
        emailid = cursor.fetchone()
        print(emailid[0])
        conn.commit()
        subject = "SmartFirm Application Rejection Mail"
        body = "Your application has been rejected..!!"
        email = EmailMessage(subject, body, to=[emailid[0]])
        email.send()
        print('done')
        return MANworkingWeekend(request)

    except Error as e:
        print(e)
        print('something is going  wrong')

    finally:
        cursor.close()
        conn.close()
    # return render(request, 'REJECTPAGE.html')
    return HttpResponse('mail is sent')

def TransportationService(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='smart_firm', user='root', password='root',auth_plugin='mysql_native_password')
        cursor = conn.cursor()

        query1 = "SELECT * FROM stations"
        cursor.execute(query1)
        s = cursor.fetchall()
        return render(request, 'CAB.html', {'s':s})
    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


    """return render(request,'CAB.html')"""

def DoTransportationServiceEMP(request):
    try:
         source = int(request.POST.get('s'))
         destination = int(request.POST.get('d'))
         ts_time = request.POST.get('time')
         ts_date = request.POST.get('date')
         ts_status = request.POST.get('desc')

         conn = mysql.connector.connect(host='localhost', database='smart_firm', user='root', password='root', auth_plugin='mysql_native_password')
         cursor = conn.cursor()

         lid = request.session.get('lid')
         print(lid)
         query1 = "SELECT emp_rid FROM emp_registration WHERE emp_lid='%d'" %(lid)
         cursor.execute(query1)
         emp = cursor.fetchone()
         e = emp[0]
         print(emp)

         query = "INSERT INTO cab_service(eid,SOURCEID ,T_DATE, STATUS , DESTINATIONID , T_TIME   ) VALUES ('%d','%d','%s','%s','%d','%s')" %(e,source,ts_date,ts_status,destination,ts_time)
         print(query)
         cursor.execute(query)
         conn.commit()

         #query1 = "select emp_rid FROM emp_reg WHERE emp_"
         return HttpResponse("CAB IS ON THE WAY...!!")
         #return render(request , 'CAB.html')

    except Error as e:
        print(e)


    finally:
        cursor.close()
        conn.close()

def Handling_cab_manager(request):
    return render(request, 'SERVICES_OF_MANAGER.html')

def Manager_cab_stauts(request):
    try:
        conn = mysql.connector.connect(host='localhost', database='smart_firm', user='root', password='root',
                                       auth_plugin='mysql_native_password')

        cursor = conn.cursor()

        qry="SELECT cs.SOURCEID, cs.T_DATE, cs.STATUS, cs.DESTINATIONID, cs.T_TIME, er.name,cs.TID  FROM cab_service as cs join emp_registration as er on cs.eid = er.emp_rid " \
            "WHERE cs.AR_STATUS='Pending'"

        cursor.execute(qry)
        rows = cursor.fetchall()
        print("data is : ", rows)
        return render(request, 'SERVICES_OF_MANAGER.html', {'rows': rows})
        #return  Handling_cab_manager(request)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def Status_acccept(request):
    try:
        id = int(request.GET.get('id'))
        #id = int(request.GET.get('emp_id'))
        conn = mysql.connector.connect(host='localhost', database='smart_firm', user='root', password='root',auth_plugin='mysql_native_password')
        cursor = conn.cursor()
        query = "UPDATE cab_service SET AR_STATUS = 'Accepted' WHERE tid='%d'" % (id)
        print(query)
        cursor.execute(query)
        conn.commit()

        qry = "SELECT l.username from login as l join emp_registration on emp_registration.emp_lid = l.lid join cab_service on emp_registration.emp_rid = cab_service.eid WHERE cab_service.tid = %d" % id
        cursor.execute(qry)
        emailid = cursor.fetchone()
        print(emailid[0])
        conn.commit()
        subject = "SmartFirm Application Acception Mail"
        body = "Your application has been Accepted..!!"
        email = EmailMessage(subject, body, to=[emailid[0]])
        email.send()
        print('done')
        return Manager_cab_stauts(request)
        #return HttpResponse("your cab request is approved by the CEO")


    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def CAB_REJECTED(request):
    try:
        id = int(request.GET.get('id'))
        conn = mysql.connector.connect(host='localhost', database='smart_firm', user='root', password='root',auth_plugin='mysql_native_password')
        cursor = conn.cursor()
        query = "UPDATE cab_service SET AR_STATUS = 'Rejected' WHERE tid='%d'" % (id)
        print(query)
        cursor.execute(query)

        qry = "SELECT l.username FROM login as l join emp_registration on emp_registration.emp_lid = l.lid join cab_service on emp_registration.emp_rid = cab_service.eid where cab_service.tid = %d" % id
        cursor.execute(qry)
        emailid = cursor.fetchone()
        print(emailid[0])
        conn.commit()
        subject = "SmartFirm Application Rejection Mail"
        body = "Your application has been rejected..!!"
        email = EmailMessage(subject, body, to=[emailid[0]])
        email.send()
        print('done')
        return Manager_cab_stauts(request)



    except Error as e:
        print(e)
        print('something is going  wrong')

    finally:
        cursor.close()
        conn.close()
    #return HttpResponse("your cab request is rejcted by the CEO")

def NotesOfConfCall(request):
    return render(request, 'CreateNote.html')

def CREATE_NOTE(request):

    note = request.POST.get('Description')
    email = request.POST.get('Email')

    subject = "SmartFirm Application video call note"
    body = note
    email = EmailMessage(subject, body, to=[email] )
    email.send()
    print('done')

    return render(request, 'CreateNote.html')

# Create your views here.

