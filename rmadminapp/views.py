#
#@author: Brian
#
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.timezone import make_aware
from django.core.mail import EmailMessage
from django.conf import settings
from rmadminapp.models import Rmemails, RmemailsForm, userList
from rmusersapp.models import Rmusers, checkFile, account2, mytimeDb, getUsers
import pprint
import json
import datetime
import time


def index(request):
    pname = 'Rmwebapp'
    ip = request.META['REMOTE_ADDR']
    now = mytime2()
    year = now.year
    ref = [0]
    users = []
    dbusers = []
    numberOfUsers = 0
    display = 3
    subject = 'RM Info.'
    try:
        users = userList({"ref": account2(ref), "email": "info@rmweb.org"})
        display = 10 if(len(users) > 10) else 5
        dbusers = getUsers()
        numberOfUsers = len(dbusers)
        if(numberOfUsers > 0):
            display = 60 if(numberOfUsers > 60) else 25
            #pprint.pprint(dbusers)
        else:
            display = 50 if(len(users) > 50) else 15
            numberOfUsers = len(users)
    except Exception as e:
        print("Rmadmin error: ", e)
    for x in users:
        dbusers.append(x)
    paginator = Paginator(dbusers, display)
    page = request.GET.get('page')
    usersinfo = paginator.get_page(page)
    return render(
        request, 'rmadmin.html', context={'pname': pname, 'message': now,
        'numberOfUsers': numberOfUsers, 'users': usersinfo, 'subject': subject,
        'ip': ip, 'year': year},
    )

ref2 = [0]
def rmsend(request):
    pname = settings.PRO_NAME
    ip = request.META['REMOTE_ADDR']
    now = mytime2()
    year = now.year
    profile = 'tmp'
    emailfrom = 'yourname@yourdomain.org'
    app = {}
    pmessage = 'rmsend...'
    ref = ''
    try:
        done = False
        ref = account2(ref2)
        print(ref, request)
        if request.method == 'POST':
            req = request.POST
            app = Rmemails()
            app.ref = ref
            app.name = req['name'].strip()
            app.surname = req['surname'].strip()
            app.emailfrom = settings.EMAIL_HOST_USER
            app.emailto = req['email'].strip()
            app.subject = req['subject'].strip()
            app.phone = req['phone'].strip()
            app.message = req['message'].strip()
            print("emailfrom: %s, %s, %s, %s"%(app.emailfrom, app.emailto, app.subject, app.ref))
            msg = EmailMessage(app.subject, app.message, app.emailfrom, [app.emailto])
            msg.content_subtype = 'html'
            file = checkFile(request, profile, ref)
            if(file != 0):
                app.attachment = file
                msg.attach_file(app.attachment)
                print(app.message)
                print(msg)
                #Send the message.
                msg.send()
                print("Message sent with: %s"%(app.attachment))
                done = True
            else:
                print(app.message)
                print(msg)
                msg.send()
                print("Message sent...")
                done = True
            if(done):
                try:
                    app.emaildate = mytimeDb()
                    #Save the message.
                    app.save()
                    print("Message saved...%s"%(app.ref))
                except Exception as e:
                    print("#2 Rmsend error: ", e)
        else:
            return redirect('/rmadmin/')
        pmessage = "Message Sent...%s"%(ref)
    except Exception as e:
        pmessage = "Rmsend error...%s %s"%(ref, e)
        print(pmessage)
    return render(
        request, 'adminfeedback.html', context={'app': app,
        'pname': pname, 'ip': ip, 'year': year, 'message': pmessage},
    )

def mytime2():
    now = datetime.datetime.now()
    dnow = make_aware(now)
    print("RM WebApp: %s-%s, %s-%s"%(now, now.tzinfo, dnow, dnow.tzinfo))
    return dnow
