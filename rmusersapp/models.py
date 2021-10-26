#
# @author: Brian
#
#from django.db import models
from djongo import models
from django import forms
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files import File
from django.utils.timezone import make_aware
from pymongo import MongoClient, InsertOne, DeleteMany, ReplaceOne, UpdateOne
import datetime
import time
import random

client = MongoClient()

def userProfile():
    rand = random.randint(1, 4)
    defaultProfile = "/rmusersapp/profile/pro%s.jpg"%(rand)
    return defaultProfile

def mytimeDb():
    #now = datetime.datetime.now()
    #dnow2 = make_aware(now)
    utcnow = datetime.datetime.utcnow()
    dnow = make_aware(utcnow)
    #dt = (dnow2 - dnow)
    #print("Users model: %s, %s"%(dnow, dt))
    return dnow


class Rmusers(models.Model):
    ref = models.CharField(max_length=250, unique=True)
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, unique=True)
    phone = models.CharField(max_length=250)
    message = models.TextField()
    userfile = models.CharField(max_length=250)
    profile = models.CharField(max_length=250, default=userProfile())
    updatedinfo = models.BooleanField(default=False)
    rmdate = models.DateTimeField()
    rmdateupdated = models.DateTimeField()
    objects = models.DjongoManager()

    def __str__(self):
        return self.name

class RmusersForm(forms.ModelForm):
    class Meta:
        model = Rmusers
        fields = (
           'name', 'surname', 'email'
        )

class UploadFile(forms.Form):
    name = forms.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    filename = forms.FileField(label=" ", label_suffix="+")

    def sanitizeFile(self):
        print("Self: %s"%(self))
        file = self.cleaned_data['filename']
        ext = file.name.split('.')[-1].lower()
        if ext not in ['jpg', 'pdf', 'png', 'txt']:
            return 0, 0
        return file, ext

def checkFile(request, folder, ref):
    if request.method == 'POST':
        try:
            req = request.POST
            req2 = request.FILES
            size = req2['filename'].size
            maxb = (1024 * 500)
            print("Size: %s, %s"%(size, maxb))
            if size > maxb:
                return 0
            form = UploadFile(req, req2)
            if form.is_valid():
                #freq = req2['filename'].file.read()
                ufile, ext =  form.sanitizeFile()
                if ext == 0:
                    return 0
                else:
                    filereq = ufile.file.read()
                    userfile = saveFile(filereq, folder, ref, ext)
                    file3 = "file: %s-%s"%(userfile, size)
                    print(file3)
                    return userfile
        except Exception as e:
            print("checkfile erro: ", e)
    return 0

def saveFile(file, folder, ref, ext):
    try:
        pfile = 'assets/%s/%s%s.%s'%(folder, folder, ref, ext)
        path = default_storage.save(pfile, ContentFile(file))
        return path
    except Exception as e:
        print("%s-%s"%(ref, e))
    return 0

def account2(ref):
    ref[0] += 1
    #d2 = mytime2b()
    d2 = mytimeDb()
    d3 = d2.microsecond
    accn = "%d%d%d%d%d%d%d"%(d2.year, d2.month, d2.day,
        d2.hour, d2.minute, d2.second, d3%1000)
    sern = int(accn) + ref[0]
    return sern

def mytime2b():
    now = datetime.datetime.now()
    return now

con = [0]
def dbConnection():
    db = {}
    try:
        print("%s dbConnection: %s"%(mytime2b(), con[0]))
        db = client.rmwebappdb
        con[0] += 1
    except Exception as e:
        print("dbConnection erro: %s, %s"%(mytime2b(), e))
    return db

def checkUser(app):
    db = {}
    try:
        db = dbConnection()
        print("checkUser: %s, %s, %s"%(mytime2b(), app.email, db))
        db3 = db.rmusersapp_rmusers.find_one({ "email": app.email })
        print("checking..%s, %s"%(db3['email'], db))
        return [db3["email"], db3, db]
    except Exception as e:
        print("checkUser error: %s %s"%(mytime2b(), e))
    return ["None", app, db]

def getUsers():
    try:
        db3 = []
        db = dbConnection()
        #numberOfUsers = db.rmusersapp_rmusers.count_documents({})
        db4 = db.rmusersapp_rmusers.find()
        x = 0
        for users in db4:
            db3.append(users)
            #db3[x]['_id'] = x+1
            db3[x]['_id'] = "%s"%(db3[x]['_id'])
            #print(db3[x]['_id'])
            x += 1
        #db5 = json.dumps(db3)
        return db3
    except Exception as e:
        print("getUsers error: ", e)
    return [{}]
