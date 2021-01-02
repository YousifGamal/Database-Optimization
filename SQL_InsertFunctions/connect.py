import mysql.connector


def Connect():
    mydb = mysql.connector.connect(
        host="localhost",
        user="newuser",
        password="password",
        database="college"
    )
    #print(mydb.autocommit)
    
    return mydb
Connect()