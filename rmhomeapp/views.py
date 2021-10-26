#
# @author: Brian
#
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.timezone import make_aware
from django.conf import settings
from rmusersapp.models import Rmusers, checkFile, account2, mytimeDb, checkUser
import pprint
import json
import datetime
import time


def index(request):
    pname = settings.PRO_NAME
    ip = request.META['REMOTE_ADDR']
    now = mytime2()
    year = now.year
    return render(
        request, 'home.html', context={'pname': pname, 'message': now,
        'ip': ip, 'year': year},
    )

ref2 = [0]
def updateinfo(request):
    pname = settings.PRO_NAME
    ip = request.META['REMOTE_ADDR']
    now = mytime2()
    year = now.year
    profile = 'update'
    ref = account2(ref2)
    print(profile, ref)
    pmessage = ref
    app = {}
    updatedb = {}
    if request.method == 'POST':
        try:
            req = request.POST
            app = Rmusers()
            app.name = req['name'].strip()
            app.surname = req['surname'].strip()
            app.email = req['email'].strip()
            app.phone = req['phone'].strip()
            app.message = req['message'].strip()
            app.updatedinfo = True
            app.rmdateupdated = mytimeDb()
            db2 = checkUser(app)
            if(db2[0] == "None"):
                pmessage = "This User: %s, Doesn't exist...#%s"%(app.email, ref)
            else:
                file = checkFile(request, profile, ref)
                app.userfile = file
                #Update info
                db3 = db2[1]
                db3['name'] = app.name
                db3['surname'] = app.surname
                db3['email'] = app.email
                db3['phone'] = app.phone
                db3['message'] = app.message
                db3['updatedinfo'] = app.updatedinfo
                db3['rmdateupdated'] = app.rmdateupdated
                db3['userfile'] = app.userfile
                #Update info using dbConnection
                updatedb = db2[2].rmusersapp_rmusers.save(db3)
                pmessage = "%s, User Updated...#%s"%(updatedb, ref)
        except Exception as e:
            pmessage = "Update User error: %s, %s, %s"%(updatedb, ref, e)
            print(pmessage)
    else:
        return redirect('/rmusers/')
    return render(
        request, 'homefeedback.html', context={'pname': pname, 'app': app,
        'message': pmessage, 'ip': ip, 'year': year, 'ref': ref},
    )

ref3 = [0]
def helpfilter(request):
    pname = settings.PRO_NAME
    ip = request.META['REMOTE_ADDR']
    now = mytime2()
    year = now.year
    profile = 'help'
    ref = account2(ref3)
    print(profile, ref)
    pmessage = "Help...%s"%(ref)
    app = {}
    if request.method == 'POST':
        try:
            req = request.POST
            app = Rmusers()
            app.email = req['emailfilter'].strip()
            db2 = checkUser(app)
            if(db2[0] == "None"):
                pmessage = "This User Doesn't exist...#%s"%(ref)
            else:
                db3 = db2[1]
                pprint.pprint(db3)
                app.ref = db3['ref']
                app.name = db3['name']
                app.surname = db3['surname']
                app.email = db3['email']
                app.phone = db3['phone']
                app.message = db3['message']
                app.updatedinfo = db3['updatedinfo']
                app.userfile = db3['userfile']
                app.rmdate = db3['rmdate']
                app.rmdateupdated = db3['rmdateupdated']
        except Exception as e:
            pmessage = "Help Error...%s %s"%(ref, e)
            print(pmessage)
    return render(
        request, 'home.html', context={'pname': pname, 'app': app,
        'message': pmessage,  'ip': ip, 'year': year},
    )

def mytime2():
    now = datetime.datetime.now()
    dnow = make_aware(now)
    utcnow = datetime.datetime.utcnow()
    unow = make_aware(utcnow)
    dt = (dnow - unow)
    print("UTC:  %s,   %s, %s-%s"%(utcnow, dt, unow, unow.tzinfo))
    print("Home: %s-%s,       %s-%s"%(now, now.tzinfo, dnow, dnow.tzinfo))
    return dnow
