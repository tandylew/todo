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
            try:
                mydb =mysql.connector.connect(host='172.18.0.1',user='root',passwd='Welcome1',database='mydb',auth_plugin='mysql_native_password')
                mycursor = mydb.cursor(buffered=True)
                mycursor.execute("SELECT * FROM todo")
                result = mycursor.fetchall()
                print(result)
            except:
                print("No results")
            return render(request, 'display_task.html', {'form': form})
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
            return HttpResponseRedirect('/display_task/')

def display_task(request):
    if request.method == 'GET':
        mydb = mysql.connector.connect(host='172.18.0.1',user='root',passwd='Welcome1',database='mydb',auth_plugin='mysql_native_password')
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("SELECT * FROM todo")
        result = mycursor.fetchall()
        return HttpResponse(result)
        #form = ContactForm(request.POST)
        #return render(request, 'display_task.html')
    elif request.method == 'POST':
        return HttpResponse("Hello Word. You're Andy")
