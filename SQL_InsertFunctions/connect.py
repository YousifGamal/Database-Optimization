import mysql.connector


def ConnectMySQL():
    mydb = mysql.connector.connect(
        host="localhost",
        user="Gellesh",
        password="khaledG123",
        database="college"
    )
    #print(mydb.autocommit)
    
    return mydb



ConnectMySQL()