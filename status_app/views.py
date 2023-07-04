from django.shortcuts import render,redirect
from pyModbusTCP.client import ModbusClient
from status_app.models import StatusTable
from datetime import date, timedelta
from io import BytesIO
from django.http import HttpResponse
import pandas as pd
from status_app.models import Emailtable,StatusTable , StatusTabletwo,StatusTable8192,StatusTable8193,StatusTable8194,StatusTable8195,StatusTable8196,StatusTable8197,StatusTable8198
import threading
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime,date
# from datetime import datetime, timedelta
import datetime
import pytz
from django.db.models import Sum

# global c
c = ModbusClient('10.1.1.100', debug=True, auto_open=True)


def readfunc(): 
    global ReadTagStatusone,ReadTagStatustwo,ReadTagStatusthree,ReadTagStatusfour,ReadTagStatusfive,ReadTagStatussix,ReadTagStatusseven
    # previous_status = None  # Initialize previous_status variable
    previous_statustwo = None
    previous_statusthree = None
    previous_statusfour = None
    previous_statusfive = None                              
    previous_statussix = None
    previous_statusseven = None
    # global c
    # c = ModbusClient('10.1.1.100', debug=True, auto_open=True)
    last_data_is = StatusTable8192.objects.values_list('TagStatus',flat=True).last()
    last_date_is = StatusTable8192.objects.values_list('TimeIs',flat=True).last()
    dateis=last_date_is.date()
    TodayDate=date.today()
    while True:   
        ReadTagStatusone = c.read_coils(8192)
        current_status = ReadTagStatusone[0]
        current_status_str=str(current_status)
 
    
        if current_status_str != last_data_is:
            DeviceNameone = '8192'
            SavingTagToDB = StatusTable8192(TagStatus=current_status, NameOfDevice=DeviceNameone)
            SavingTagToDB.save()
        
            last_data_is = current_status_str  # Update previous_status

        if dateis != TodayDate:
            DeviceNameone = '8192'
            SavingTagToDB = StatusTable8192(TagStatus=current_status, NameOfDevice=DeviceNameone)
            SavingTagToDB.save()
            dateis = TodayDate     

        ReadTagStatustwo = c.read_coils(8193)
        current_statustwo = ReadTagStatustwo[0]
      
        if current_statustwo != previous_statustwo or previous_statustwo is None:
            DeviceNametwo = '8193'
            SavingTagToDBtwo = StatusTable8193(TagStatus=current_statustwo, NameOfDevice=DeviceNametwo)
            SavingTagToDBtwo.save()
            
        previous_statustwo = current_statustwo   
 
            
        ReadTagStatusthree = c.read_coils(8194)
        current_statusthree = ReadTagStatusthree[0]
        

        if current_statusthree != previous_statusthree or previous_statusthree is None:
            DeviceNamethree = '8194'
            SavingTagToDBthree = StatusTable8194(TagStatus=current_statusthree, NameOfDevice=DeviceNamethree)
            SavingTagToDBthree.save()   
        
        previous_statusthree = current_statusthree
        
        
        ReadTagStatusfour = c.read_coils(8195)
        current_statusfour = ReadTagStatusfour[0]
        

        if current_statusfour != previous_statusfour or previous_statusfour is None:
            DeviceNamefour = '8195'
            SavingTagToDBfour = StatusTable8195(TagStatus=current_statusfour, NameOfDevice=DeviceNamefour)
            SavingTagToDBfour.save()   
        
        previous_statusfour = current_statusfour
        
        ReadTagStatusfive = c.read_coils(8196)
        current_statusfive = ReadTagStatusfive[0]
        

        if current_statusfive != previous_statusfive or previous_statusfive is None:
            DeviceNamefive = '8196'
            SavingTagToDBfive = StatusTable8196(TagStatus=current_statusfive, NameOfDevice=DeviceNamefive)
            SavingTagToDBfive.save()   
        
        previous_statusfive = current_statusfive
        
        
        
        ReadTagStatussix = c.read_coils(8197)
        current_statussix = ReadTagStatussix[0]
        

        if current_statussix != previous_statussix or previous_statussix is None:
            DeviceNamesix = '8197'
            SavingTagToDBsix = StatusTable8197(TagStatus=current_statussix, NameOfDevice=DeviceNamesix)
            SavingTagToDBsix.save()   
        
        previous_statussix = current_statussix
        
        
        
        ReadTagStatusseven = c.read_coils(8198)
        current_statusseven = ReadTagStatusseven[0]
        

        if current_statusseven != previous_statusseven or previous_statusseven is None:
            DeviceNameseven = '8198'
            SavingTagToDBseven = StatusTable8198(TagStatus=current_statusseven, NameOfDevice=DeviceNameseven)
            SavingTagToDBseven.save()   
        
        previous_statusseven = current_statusseven

  
        time.sleep(10)
 
def RunReadFuncThread():
    job_thread = threading.Thread(target=readfunc)
    job_thread.start()
      
RunReadFuncThread()    
def Mailfunc(): 
    previous_status_email = None  # Store the previous status
    while True:   
        EmailStatus = c.read_coils(8199)
        EmailStatusIndex = EmailStatus[0]
        print(EmailStatusIndex)
        if previous_status_email is not None and EmailStatusIndex != previous_status_email:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("rathorabhay633@gmail.com", "amuleezkgefwacah")

            subject = "Testing male module "
            if EmailStatusIndex == True:
                message = "Sending mail to check EmailStatusIndex is true"
            else:
                message = "Sending mail to check EmailStatusIndex is false"
                
            EmailData=Emailtable.objects.all()
            email_list = [email.EmailInModel for email in EmailData]
            tosenders=email_list

            msg = MIMEMultipart()
            msg['From'] = "rathorabhay633@gmail.com"
            msg['To'] = ", ".join(tosenders)
            msg['Subject'] = subject

            msg.attach(MIMEText(message, 'plain'))

            s.send_message(msg)
            s.quit()
        else:
            print("nothing")    
        
        previous_status_email = EmailStatusIndex  # Update the previous status
        time.sleep(10)

# Running Analog Function in a Separate Thread 
def MailThreading():
    job_thread_E = threading.Thread(target=Mailfunc)
    job_thread_E.start()

def StatusPageFunc(request):
        
    MailThreading()    

    # RunReadFuncThread() 
    # ReadTagStatusone=45
    # ReadTagStatustwo=45
    # ReadTagStatusthree=15
    # ReadTagStatusfour=96
    # ReadTagStatusfive=12
    # ReadTagStatussix=354
    # ReadTagStatusseven=45
    context={
        'ReadTagStatusone':ReadTagStatusone,
        'ReadTagStatustwo':ReadTagStatustwo,
        'ReadTagStatusthree':ReadTagStatusthree,
        'ReadTagStatusfour':ReadTagStatusfour,
        'ReadTagStatusfive':ReadTagStatusfive,
        'ReadTagStatussix':ReadTagStatussix,
        'ReadTagStatusseven':ReadTagStatusseven,
        # 'ReadTagStatuseight':ReadTagStatuseight,
    }

    return render(request ,'status.html',context)

def ReportPageFunc(request):
    return render(request ,'Report.html')
    


def ReportFunc(request):
    if request.method == "POST":
        ManualWeekdaysStart = request.POST.get('start')
        print(ManualWeekdaysStart, "start day")
        ManualWeekdaysStartVal = str(ManualWeekdaysStart)
        ManualWeekDaysEnd = request.POST.get('end')
        print(ManualWeekDaysEnd, "END day")
        ManualWeekDaysEndVal = str(ManualWeekDaysEnd)
        datais = request.POST.get('start2')
        print(datais, "list wala")
        DeviceNameFromFrontend = request.POST.get('deviceselection')
        print(DeviceNameFromFrontend)
        if DeviceNameFromFrontend == 'device1':
            DBis = StatusTable8192
        elif DeviceNameFromFrontend == 'device2':
            DBis = StatusTable8193
        elif DeviceNameFromFrontend == 'device3':
            DBis = StatusTable8194
        elif DeviceNameFromFrontend == 'device4':
            DBis = StatusTable8195
        elif DeviceNameFromFrontend == 'device5':
            DBis = StatusTable8196
        elif DeviceNameFromFrontend == 'device6':
            DBis = StatusTable8197
        elif DeviceNameFromFrontend == 'device7':
            DBis = StatusTable8198
        else:
            print("NOTHING")
        

    if datais == 'week':
        startdate = date.today()
        StartDateForWeeksList = str(startdate)
        enddate = startdate - timedelta(days=7)
        EndDateForWeeksList = str(enddate)
        ReportDataWeek=DBis.objects.values().filter(TimeIs__date__range=[EndDateForWeeksList,StartDateForWeeksList]) 
        with BytesIO() as b:
                writer = pd.ExcelWriter(b, engine='xlsxwriter')
                df = pd.DataFrame(ReportDataWeek)
                df['TimeIs'] = df['TimeIs'].astype(str)
                df['TimeIs'] = pd.to_datetime(df.TimeIs).dt.tz_localize(None)
                result=df.dtypes
                df2 = df.copy()
                df2.to_excel(writer, sheet_name='Sheet1')
                writer.save()       
                x = date.today().strftime("%y-%m-%d")
                filename = 'Report.xlsx'
                response = HttpResponse(
                b.getvalue(),
                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
                response['Content-Disposition'] = 'attachment; filename=%s' % filename 
                return response

    elif datais == 'month':
        startdate = date.today()
        StartDateForWeeksList = str(startdate)
        enddate = startdate - timedelta(days=31)
        EndDateForWeeksList = str(enddate)
        ReportDataMonth=DBis.objects.values().filter(TimeIs__date__range=[EndDateForWeeksList,StartDateForWeeksList]) 
        with BytesIO() as b:
                writer = pd.ExcelWriter(b, engine='xlsxwriter')
                df = pd.DataFrame(ReportDataMonth)
                df['TimeIs'] = df['TimeIs'].astype(str)
                df['TimeIs'] = pd.to_datetime(df.TimeIs).dt.tz_localize(None)
                result=df.dtypes
                df2 = df.copy()
                df2.to_excel(writer, sheet_name='Sheet1')
                writer.save()       
                x = date.today().strftime("%y-%m-%d")
                filename = 'Report.xlsx'
                response = HttpResponse(
                b.getvalue(),
                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
                response['Content-Disposition'] = 'attachment; filename=%s' % filename 
                return response

    elif datais == 'half_year':
        startdate = date.today()
        StartDateForWeeksList = str(startdate)
        enddate = startdate - timedelta(days=180)
        EndDateForWeeksList = str(enddate)
        ReportDataHalfyear=DBis.objects.values().filter(TimeIs__date__range=[EndDateForWeeksList,StartDateForWeeksList]) 
        with BytesIO() as b:
                writer = pd.ExcelWriter(b, engine='xlsxwriter')
                df = pd.DataFrame(ReportDataHalfyear)
                df['TimeIs'] = df['TimeIs'].astype(str)
                df['TimeIs'] = pd.to_datetime(df.TimeIs).dt.tz_localize(None)
                result=df.dtypes
                df2 = df.copy()
                df2.to_excel(writer, sheet_name='Sheet1')
                writer.save()       
                x = date.today().strftime("%y-%m-%d")
                filename = 'Report.xlsx'
                response = HttpResponse(
                b.getvalue(),
                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
                response['Content-Disposition'] = 'attachment; filename=%s' % filename 
                return response

    elif datais == 'year':
        startdate = date.today()
        StartDateForWeeksList = str(startdate)
        enddate = startdate - timedelta(days=365)
        EndDateForWeeksList = str(enddate)
        ReportDataYear=DBis.objects.values().filter(TimeIs__date__range=[EndDateForWeeksList,StartDateForWeeksList]) 
        with BytesIO() as b:
                writer = pd.ExcelWriter(b, engine='xlsxwriter')
                df = pd.DataFrame(ReportDataYear)
                df['TimeIs'] = df['TimeIs'].astype(str)
                df['TimeIs'] = pd.to_datetime(df.TimeIs).dt.tz_localize(None)
                result=df.dtypes
                df2 = df.copy()
                df2.to_excel(writer, sheet_name='Sheet1')
                writer.save()       
                x = date.today().strftime("%y-%m-%d")
                filename = 'Report.xlsx'
                response = HttpResponse(
                b.getvalue(),
                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
                response['Content-Disposition'] = 'attachment; filename=%s' % filename 
                return response
    else:

       ManulReport=DBis.objects.values().filter(TimeIs__date__range=[ManualWeekDaysEndVal,ManualWeekdaysStartVal])
       with BytesIO() as b:
                writer = pd.ExcelWriter(b, engine='xlsxwriter')
                df = pd.DataFrame(ManulReport)
                df['TimeIs'] = df['TimeIs'].astype(str)
                df['TimeIs'] = pd.to_datetime(df.TimeIs).dt.tz_localize(None)
                result=df.dtypes
                df2 = df.copy()
                df2.to_excel(writer, sheet_name='Sheet1')
                writer.save()       
                x = date.today().strftime("%y-%m-%d")
                filename = 'Report.xlsx'
                response = HttpResponse(
                b.getvalue(),
                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
                response['Content-Disposition'] = 'attachment; filename=%s' % filename 
                return response
    return render(request, 'Report.html')

def AnalyticsFunc(request):
    

    timezone = pytz.timezone('Asia/Calcutta')
    now = datetime.datetime.now(tz = timezone)
    print(now)  
    time_format = '%Y-%m-%d %H:%M:%S.%f'
    
    last_row = StatusTable8192.objects.latest('TimeIs')
    last_row_data = (last_row.TagStatus, last_row.NameOfDevice, last_row.TimeIs)
    last_row_time_str = last_row_data[2].strftime(time_format)  
    last_row_time = datetime.datetime.strptime(last_row_time_str, time_format).astimezone(timezone)
    time_difference_minutes = 0.1
    time_difference_minutes_false = 0.1
    if last_row_data[0] == 'True':
        time_difference = now - last_row_time
        time_difference_minutes = int(time_difference.total_seconds() / 60)
        # time_difference_str=str(time_difference).split('.')[0]
    else:
        time_difference_false = now - last_row_time
        time_difference_minutes_false = int(time_difference_false.total_seconds() / 60)

    last_row8193 = StatusTable8193.objects.latest('TimeIs')
    last_row_data_8193 = (last_row8193.TagStatus, last_row8193.NameOfDevice, last_row8193.TimeIs)
    last_row_time_str_8193 = last_row_data_8193[2].strftime(time_format)  
    last_row_time_8193 = datetime.datetime.strptime(last_row_time_str_8193, time_format).astimezone(timezone)
    time_difference_minutes_8193 = 0.1
    time_difference_minutes_false_8193 = 0.1
    if last_row_data_8193[0] == 'True':
        time_difference_8193 = now - last_row_time_8193
        time_difference_minutes_8193 = int(time_difference_8193.total_seconds() / 60)
    else:
        time_difference_false_8193 = now - last_row_time_8193
        time_difference_minutes_false_8193 = int(time_difference_false_8193.total_seconds() / 60) 
        
        
    last_row8194 = StatusTable8194.objects.latest('TimeIs')
    last_row_data_8194 = (last_row8194.TagStatus, last_row8194.NameOfDevice, last_row8194.TimeIs)
    last_row_time_str_8194 = last_row_data_8194[2].strftime(time_format)  
    last_row_time_8194 = datetime.datetime.strptime(last_row_time_str_8194, time_format).astimezone(timezone)
    time_difference_minutes_8194 = 0.1
    time_difference_minutes_false_8194 = 0.1
    if last_row_data_8194[0] == 'True':
        time_difference_8194 = now - last_row_time_8194
        time_difference_minutes_8194 = int(time_difference_8194.total_seconds() / 60)
    else:
        time_difference_false_8194 = now - last_row_time_8194
        time_difference_minutes_false_8194 = int(time_difference_false_8194.total_seconds() / 60) 
        
        
    last_row8195 = StatusTable8195.objects.latest('TimeIs')
    last_row_data_8195 = (last_row8195.TagStatus, last_row8195.NameOfDevice, last_row8195.TimeIs)
    last_row_time_str_8195 = last_row_data_8195[2].strftime(time_format)  
    last_row_time_8195 = datetime.datetime.strptime(last_row_time_str_8195, time_format).astimezone(timezone)
    time_difference_minutes_8195 = 0.1
    time_difference_minutes_false_8195 = 0.1
    if last_row_data_8195[0] == 'True':
        time_difference_8195 = now - last_row_time_8195
        time_difference_minutes_8195 = int(time_difference_8195.total_seconds() / 60)
    else:
        time_difference_false_8195 = now - last_row_time_8195
        time_difference_minutes_false_8195 = int(time_difference_false_8195.total_seconds() / 60)
     
     
    last_row8196 = StatusTable8196.objects.latest('TimeIs')
    last_row_data_8196 = (last_row8196.TagStatus, last_row8196.NameOfDevice, last_row8196.TimeIs)
    last_row_time_str_8196 = last_row_data_8196[2].strftime(time_format)  
    last_row_time_8196 = datetime.datetime.strptime(last_row_time_str_8196, time_format).astimezone(timezone)
    time_difference_minutes_8196 = 0.1
    time_difference_minutes_false_8196 = 0.1
    if last_row_data_8196[0] == 'True':
        time_difference_8196 = now - last_row_time_8196
        time_difference_minutes_8196 = int(time_difference_8196.total_seconds() / 60)
    else:
        time_difference_false_8196 = now - last_row_time_8196
        time_difference_minutes_false_8196 = int(time_difference_false_8196.total_seconds() / 60)
       
       
    last_row8197 = StatusTable8197.objects.latest('TimeIs')
    last_row_data_8197 = (last_row8197.TagStatus, last_row8197.NameOfDevice, last_row8197.TimeIs)
    last_row_time_str_8197 = last_row_data_8197[2].strftime(time_format)  
    last_row_time_8197 = datetime.datetime.strptime(last_row_time_str_8197, time_format).astimezone(timezone)
    time_difference_minutes_8197 = 0.1
    time_difference_minutes_false_8197 = 0.1
    if last_row_data_8197[0] == 'True':
        time_difference_8197 = now - last_row_time_8197
        time_difference_minutes_8197 = int(time_difference_8197.total_seconds() / 60)
    else:
        time_difference_false_8197 = now - last_row_time_8197
        time_difference_minutes_false_8197 = int(time_difference_false_8197.total_seconds() / 60)
       
    
    last_row8198 = StatusTable8198.objects.latest('TimeIs')
    last_row_data_8198 = (last_row8198.TagStatus, last_row8198.NameOfDevice, last_row8198.TimeIs)
    last_row_time_str_8198 = last_row_data_8198[2].strftime(time_format)  
    last_row_time_8198 = datetime.datetime.strptime(last_row_time_str_8198, time_format).astimezone(timezone)
    time_difference_minutes_8198 = 0.1
    time_difference_minutes_false_8198 = 0.1
    if last_row_data_8198[0] == 'True':
        time_difference_8198 = now - last_row_time_8198
        time_difference_minutes_8198 = int(time_difference_8198.total_seconds() / 60)
    else:
        time_difference_false_8198 = now - last_row_time_8198
        time_difference_minutes_false_8198 = int(time_difference_false_8198.total_seconds() / 60)                
        
        
        
   

    context={
        'time_difference_minutes': time_difference_minutes,
        'time_difference_minutes_false':time_difference_minutes_false,
        'time_difference_minutes_8193':time_difference_minutes_8193,
        'time_difference_minutes_false_8193': time_difference_minutes_false_8193,
        'time_difference_minutes_8194':time_difference_minutes_8194,
        'time_difference_minutes_false_8194': time_difference_minutes_false_8194,
        'time_difference_minutes_8195':time_difference_minutes_8195,
        'time_difference_minutes_false_8195': time_difference_minutes_false_8195,
        'time_difference_minutes_8196':time_difference_minutes_8196,
        'time_difference_minutes_false_8196': time_difference_minutes_false_8196,
        'time_difference_minutes_8197':time_difference_minutes_8197,
        'time_difference_minutes_false_8197': time_difference_minutes_false_8197,
        'time_difference_minutes_8198':time_difference_minutes_8198,
        'time_difference_minutes_false_8198': time_difference_minutes_false_8198,
    }
    return render(request,'Analytics.html',context)




def Emailfunc(request):
    EmailData=Emailtable.objects.all()
    context={
        'EmailData':EmailData,
        
    }
    
    if request.method=="POST":
        email= request.POST.get("Email")
        emaildb=Emailtable(EmailInModel=email)
        emaildb.save()
        
    return render(request,'Email.html',context)


def deleteemail(request,id):
    alldata = Emailtable.objects.get(id=id)
    alldata.delete()
    return redirect(Emailfunc)




def TotaltimeFunc(request):
    ManualStart = request.POST.get('start')
    print(ManualStart, "start day")
    ManualStartVal = str(ManualStart)
    ManualEnd = request.POST.get('end')
    print(ManualEnd, "END day")
    ManualEndVal = str(ManualEnd)
    DeviceNameFromFrontend = request.POST.get('deviceselection')
    print(DeviceNameFromFrontend)
    if DeviceNameFromFrontend == 'device1':
        DBis = StatusTable8192
    elif DeviceNameFromFrontend == 'device2':
        DBis = StatusTable8193
    elif DeviceNameFromFrontend == 'device3':
        DBis = StatusTable8194
    elif DeviceNameFromFrontend == 'device4':
        DBis = StatusTable8195
    elif DeviceNameFromFrontend == 'device5':
        DBis = StatusTable8196
    elif DeviceNameFromFrontend == 'device6':
        DBis = StatusTable8197
    elif DeviceNameFromFrontend == 'device7':
        DBis = StatusTable8198
    else:
        print("NOTHING")
        

    filtered_data = DBis.objects.filter(TimeIs__date__range=[ManualStartVal, ManualEndVal])

    total_duration = timedelta()  # Initialize total duration as zero

    for data in filtered_data:
        if data.TagStatus == 'True':
            time_is = data.TimeIs
            next_data = filtered_data.filter(TimeIs__gt=time_is).order_by('TimeIs').first()

            if next_data and next_data.TagStatus == 'False':
                time_difference = next_data.TimeIs - time_is
                total_duration += timedelta(hours=time_difference.seconds // 3600,
                                           minutes=(time_difference.seconds // 60) % 60,
                                           seconds=time_difference.seconds % 60)
    
    print("Total Time: ", total_duration)
    context={
        'total_duration':total_duration,
    }
    
    return render(request,"Report.html",context)
    
  
    
    
    
    
    
    






    
    
    
