from django.shortcuts import render
import mysql.connector
from mysql.connector import errorcode

try:
	cnx = mysql.connector.connect(user='root', password='1234', port='3306', database='world')
	print ("success")
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Something is wrong with your user name or password")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist")
	else:
		print(err)
else:
	cnx.close()


# Create your views here.

def home(request):
	cnx.reconnect()
	cursor = cnx.cursor()
	cursor.execute("select name from city")


	return render(request,'home.html',{'linha':cursor})
