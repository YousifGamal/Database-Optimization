import mysql.connector


def ConnectMySQL():
    mydb = mysql.connector.connect(
        host="localhost",
        user="newuser",
        password="password",
        database="college"
    )
    #print(mydb.autocommit)
    
    return mydb