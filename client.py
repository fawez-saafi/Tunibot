import mysql
mydb = mysql.connector.connect(host="127.0.0.1", user="root", database="chatbot")
from datetime import datetime
mycursor = mydb.cursor()

def recup_nom(name):
    mycursor.execute('''INSERT INTO client SET name=%s''', (name,))
def recup_teleph(number):
    mycursor.execute('''INSERT INTO client SET phonenumber=%s''',(number,))
def recup_date():
    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")
    mycursor.execute('''INSERT INTO client SET date=%s''',(date,))
