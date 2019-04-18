from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, loader
from django import forms
from django.db import connection
import mysql.connector
from .forms import DateForm
from json import JSONEncoder
import urllib.request
import datetime


def index(request):
        if request.method == 'GET':
            form = DateForm(request.POST)
            return render(request, 'login.html', {'form': form})
            #return HttpResponse("Hello Word. You're Andy")
        elif request.method == 'POST':
            mydb = mysql.connector.connect(host='172.18.0.1',user='root',passwd='Welcome1',database='mydb',auth_plugin='mysql_native_password')
            mycursor = mydb.cursor(buffered=True)
            #mycursor.execute("SHOW DATABASES")
            #result = mycursor.fetchall()
            response = request.read().decode().split('&')
            todo = response[1][response[1].find('=')+1:]
            month = response[2][response[2].find('=')+1:]
            day = response[3][response[3].find('=')+1:]
            year = response[4][response[4].find('=')+1:]
            mycursor.execute("CREATE TABLE IF NOT EXISTS todo (todo VARCHAR(255), due_date DATE)")
            mycursor.execute('INSERT INTO todo VALUES (%s,%s)', (todo,year+"-"+month+"-"+day))
            mycursor.execute("COMMIT")
            #result = mycursor.fetchall()
            #return HttpResponse(todo + "<br>" + month +"/" + day + "/" + year)
            #return HttpResponse("Hello Word. You're Andy")
            #connection.cursor().execute("INSERT INTO list VALUES(%s)", request.POST['email'])
            return HttpResponseRedirect('/create_list/')

def create_list(request):
    if request.method == 'GET':
        mydb =mysql.connector.connect(host='172.18.0.1',user='root',passwd='Welcome1',database='mydb',auth_plugin='mysql_native_password')
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("SELECT * FROM todo")
        result = mycursor.fetchall()
        return HttpResponse(result)
        #form = ContactForm(request.POST)
        #return render(request, 'create_list.html')
    elif request.method == 'POST':
        requestBody = JSONEncoder().encode({ '__metadata': { 'type': 'SP.List' }, 'BaseTemplate': 100, 'Title': 'Test'})
        r = s.post("https://biascorp.sharepoint.com/sites/OfficeDepot/_api/web/lists",data=requestBody)
        return HttpResponseRedirect('/delete_list/')

def create_list_item(request):
    s = sharepy.load()
    if request.method == 'GET':
        form = ContactForm(request.POST)
        return render(request, 'list_item.html')
    elif request.method == 'POST':
        requestBody = JSONEncoder().encode({ '__metadata': { 'type': 'SP.Data.TestListItem' }, 'Title': 'Test'})
        r = s.post("https://biascorp.sharepoint.com/sites/OfficeDepot/_api/web/lists/GetByTitle('Test')/items",data=requestBody)
        return HttpResponse(r.text)
    #r = s.getfile('https://biascorp.sharepoint.com/_layouts/15/userphoto.aspx?size=L&accountname=i%3A0%23.f%7Cmembership%7C' + s.username, filename='todo/output.jpg')
    #image_data = open("todo/output.jpg", "rb").read()
    #return HttpResponse(image_data, content_type="image/jpeg")
    #return HttpResponse("Hello Word. You're Andy")

def delete_list(request):
    s = sharepy.load()
    if request.method == 'GET':
        form = ContactForm(request.POST)
        return render(request, 'delete_list.html')
    elif request.method == 'POST':
        r = s.post("https://biascorp.sharepoint.com/sites/OfficeDepot/_api/web/lists/GetByTitle('Test')",headers={"X-HTTP-Method": "DELETE","If-Match": "*"})
        return HttpResponse(r.text)
