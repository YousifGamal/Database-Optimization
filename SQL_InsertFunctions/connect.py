import mysql.connector


def ConnectMySQL(database_schema):
    mydb = mysql.connector.connect(
        host="localhost",
        user="Gellesh",
        password="password",
        database=database_schema
    )
    #print(mydb.autocommit)
    
    return mydb



ConnectMySQL()
