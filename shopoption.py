import mysql.connector

mydb = mysql.connector.connect(host="127.0.0.1", user="root", database="chatbot")
mycursor = mydb.cursor()
def products():


    mycursor.execute("""select * FROM chatbot""")
    rsult = mycursor.fetchall()
    l = []
    for i in rsult:
        l.append(i[0])
    return(l)

def shopoption(reponse):
    response = reponse.split(" ")

    for i in response :
        if i in products():
            stmt = "select * from chatbot WHERE type=?"
            mycursor.execute("""select * FROM chatbot WHERE Type = %s""", (i,))
            rsult = mycursor.fetchall()
            for i in rsult:
                return "do you want to buy {} processeur :{} \n memory {} \n graphic card:{} \n color :{} \n for {}".format(i[0],i[1],i[2],i[3],i[5],i[4])
