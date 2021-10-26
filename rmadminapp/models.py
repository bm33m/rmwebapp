#
# @author: Brian
#
#from django.db import models
from djongo import models
from django import forms
from rmusersapp.models import account2, userProfile
import pprint
import json

class Rmemails(models.Model):
    ref = models.CharField(max_length=250, unique=True)
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    emailfrom = models.EmailField(max_length=250)
    emailto = models.EmailField(max_length=250)
    emailcc = models.EmailField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    attachment = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    emaildate = models.DateTimeField()
    objects = models.DjongoManager()

    def __str__(self):
        return self.subject

class RmemailsForm(forms.ModelForm):
    class Meta:
        model = Rmemails
        fields = (
           'emailfrom', 'emailto', 'subject', 'message'
        )

def userList(arg):
    ref = [1]
    info3 = [arg, {'ref': account2(ref), 'name': 'Look1', 'surname': 'Cool1', 'email': 'look1@cool.org', 'updatedinfo': False},
        {'ref': account2(ref), 'name': 'Pro1', 'surname': 'Rop1', 'email': 'pro1@rop.org'},
        {'ref': account2(ref), 'name': 'Supp1', 'surname': 'Plus1', 'email': 'supp1@plus.org', 'profile': userProfile()},
        {'ref': account2(ref), 'name': 'Cate1', 'surname': 'Gories1', 'email': 'cate1@gories.org', 'profile': userProfile()},
        {'ref': account2(ref), 'name': 'Ned1', 'surname': 'Wendy1', 'email': 'ned1@wendy.org','phone': '012 345 6789', 'updatedinfo': True, 'profile': userProfile()},
        {'ref': account2(ref), 'name': 'Gro1', 'surname': 'Pop1', 'email': 'gro1@pop.org', 'profile': userProfile()},
        {'ref': account2(ref), 'name': 'Xupp1', 'surname': 'Clus1', 'email': 'xupp1@clus.org', 'profile': userProfile()},
        {'ref': account2(ref), 'name': 'Pro2', 'surname': 'Rop2', 'email': 'pro2@rop.org'},
        {'ref': account2(ref), 'name': 'Supp2', 'surname': 'Plus2', 'email': 'supp2@plus.org', 'profile': userProfile()},
        {'ref': account2(ref), 'name': 'Cate2', 'surname': 'Gories2', 'email': 'cate2@gories.org', 'profile': userProfile()},
        {'ref': account2(ref), 'name': 'Ned2', 'surname': 'Wendy2', 'email': 'ned2@wendy.org','phone': '012 345 6782', 'updatedinfo': True, 'profile': userProfile()},
        {'ref': account2(ref), 'name': 'Gro2', 'surname': 'Pop2', 'email': 'gro2@pop.org', 'profile': userProfile()},
        {'ref': account2(ref), 'name': 'Xupp2', 'surname': 'Clus2', 'email': 'xupp2@clus.org', 'profile': userProfile()},
        {'ref': account2(ref), 'name': 'Pro3', 'surname': 'Rop3', 'email': 'pro3@rop.org'},
        {'ref': account2(ref), 'name': 'Supp3', 'surname': 'Plus3', 'email': 'supp3@plus.org', 'profile': userProfile()},
        {'ref': account2(ref), 'name': 'Cate3', 'surname': 'Gories3', 'email': 'cate3@gories.org', 'profile': userProfile()},
        {'ref': account2(ref), 'name': 'Ned3', 'surname': 'Wendy3', 'email': 'ned3@wendy.org','phone': '012 345 6783', 'updatedinfo': True, 'profile': userProfile()},
        {'ref': account2(ref), 'name': 'Gro3', 'surname': 'Pop3', 'email': 'gro3@pop.org', 'profile': userProfile()},
        {'ref': account2(ref), 'name': 'Xupp3', 'surname': 'Clus3', 'email': 'xupp3@clus.org', 'profile': userProfile()},
    ]
    return info3
