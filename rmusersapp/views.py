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
        request, 'rmusers.html', context={'pname': pname, 'message': now,
        'ip': ip, 'year': year},
    )

ref2 = [0]
def newusers(request):
    pname = settings.PRO_NAME
    ip = request.META['REMOTE_ADDR']
    now = mytime2()
    year = now.year
    profile = 'profile'
    ref = account2(ref2)
    print(profile, ref)
    pmessage = ref
    app = {}
    if request.method == 'POST':
        try:
            req = request.POST
            app = Rmusers()
            app.ref = ref
            app.name = req['name'].strip()
            app.surname = req['surname'].strip()
            app.email = req['email'].strip()
            app.phone = req['phone'].strip()
            app.message = req['message'].strip()
            db2 = checkUser(app)
            if(db2[0] == "None"):
                file = checkFile(request, profile, ref)
                app.userfile = file
                app.rmdate = mytimeDb()
                app.save()
                pmessage = "Welcome to %s, @%s...#%s"%(pname, app.name, ref)
            else:
                pmessage = "%s, Already Exist...#%s"%(app.email, ref)
        except Exception as e:
            pmessage = "New User error: %s, %s"%(ref, e)
            print(pmessage)
    else:
        return redirect('/rmusers/')
    return render(
        request, 'feedback.html', context={'pname': pname, 'app': app,
        'ref': ref, 'message': pmessage, 'ip': ip, 'year': year},
    )

def mytime2():
    now = datetime.datetime.now()
    dnow = make_aware(now)
    print("Users: %s-%s, %s-%s"%(now, now.tzinfo, dnow, dnow.tzinfo))
    return dnow
