import sqlite3


connection = sqlite3.connect("sqlite.db")

cursor = connection.cursor()

# create table
cursor.execute("""CREATE TABLE shipment(
    id INTEGER, 
    content TEXT,
    weight REAL,
    status TEXT  
    )""") 
    
    
connection.close()