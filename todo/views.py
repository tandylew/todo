from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, loader
from django import forms
from django.db import connection
import mysql.connector
import matplotlib.pyplot as plt
from .forms import DateForm, SqlForm
from json import JSONEncoder
import urllib.request
import datetime
import re


def index(request):
        if request.method == 'GET':
            form = DateForm(request.POST)
            sql = SqlForm(request.POST)
            try:
                mydb =mysql.connector.connect(host='172.18.0.1',user='root',passwd='Welcome1',database='mydb',auth_plugin='mysql_native_password')
                mycursor = mydb.cursor(buffered=True)
                mycursor.execute("SELECT * FROM todo")
                result = mycursor.fetchall()
            except:
                print("No results")
            return render(request, 'create_task.html', {'form': form, 'sql': sql})
            #return HttpResponse("Hello Word. You're Andy")
        elif request.method == 'POST':
            #print(request.body)
            #print(vars(request))
            mydb = mysql.connector.connect(host='172.18.0.1',user='root',passwd='Welcome1',database='mydb',auth_plugin='mysql_native_password')
            mycursor = mydb.cursor(buffered=True)
            #mycursor.execute("SHOW DATABASES")
            #result = mycursor.fetchall()
            response = request.read().decode().split('&')
            sql_query = response[0][response[0].find('=')+1:]
            if len(response) <= 2:
                    mycursor.execute(re.sub('\+',' ',sql_query))
                    mycursor.execute("COMMIT")
                    #print("Hello World. You're Andy")
                    #mycursor.execute()
                    #mycursor.execute("COMMIT")
            else:
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
        mycursor = mydb.cursor(buffered=True,dictionary=True)
        mycursor.execute("SELECT * FROM todo")
        result = mycursor.fetchall()
        return render(request, 'display_task.html', {'task_list': result})
        #return HttpResponse(result)
        #form = ContactForm(request.POST)
        #return render(request, 'display_task.html')
    elif request.method == 'POST':
        return HttpResponse("Hello Word. You're Andy")

def graph(request):
    if request.method == 'GET':
        plt.plot(range(20))
        plt.savefig("todo/graph.png")
        image_data = open("todo/graph.png", "rb").read()
        return HttpResponse(image_data, content_type="image/png")

def park(request):
    if request.method == 'GET':
        image_data = open("todo/park.jpg", "rb").read()
        return HttpResponse(image_data, content_type="image/jpg")
