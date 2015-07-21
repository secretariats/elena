from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, render
import datetime
from datetime import date
from time import strftime
from django.template import RequestContext
import json
import urllib, urllib2
from django.http import HttpResponseRedirect
from django.core.files import File
import os
import os.path
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from operator import itemgetter
import subprocess
from bs4 import BeautifulSoup
from dateutil.parser import parse


# Create your views here.


def calendar(request):
	return render(request, 'calendar.html')


def home(request):
	return render(request, 'birthday.html')