import mysql.connector


def ConnectMySQL(database_schema):
    mydb = mysql.connector.connect(
        host="localhost",
        user="newuser",
        password="password",
        database=database_schema
    )
    #print(mydb.autocommit)
    
    return mydb