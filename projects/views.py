from django.shortcuts import render

from projects.models import Project
from accounts.models import UserProfile, authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, HttpResponseNotFound

from django.core import serializers
import smtplib
import logging
from smtplib import SMTPRecipientsRefused

@authenticate
def create_project(request):
    def render_page():
        return render(request, 'projects/create_project.html')
        
    if request.method == 'POST':
        description_name = request.POST.get('description-name')
        location_name = request.POST.get('location-name')
        
        if request.user.is_authenticated():
            current_user_profile = request.user
        
        users = UserProfile.objects.all()
        for user in users:
            if user!=current_user_profile:
                to = user.email()
                gmail_user = 'meetupconfirm@gmail.com'
                gmail_pwd = 'dum04sci'
                smtpserver = smtplib.SMTP("smtp.gmail.com",587)
                smtpserver.ehlo()
                smtpserver.starttls()
                smtpserver.ehlo
                smtpserver.login(gmail_user, gmail_pwd)
                header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:' + description_name+ '\n' 
                msg = header + """\n Hey Guys, \n \n Let's go play in 30 minutes at the """ + location_name+ """ \n\n See you there, \n """+current_user_profile.username
                smtpserver.sendmail(gmail_user, to, msg)
                smtpserver.close()
        return redirect('main.views.home')
        return render_page('Event Created!')


    