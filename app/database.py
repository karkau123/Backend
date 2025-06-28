import sqlite3


connection = sqlite3.connect("sqlite.db")

cursor = connection.cursor()

# 1.create table
cursor.execute("""CREATE TABLE IF NOT EXISTS shipment(
    id INTEGER, 
    content TEXT,
    weight REAL,
    status TEXT  
    )""")
# 2.add shipment data
cursor.execute("""
               INSERT INTO shipment
               VALUES(12345, "Palm Trees", 8.5, 'placed')          
               """)
connection.commit()

# 3. Read a shipment by id

cursor = cursor.execute("""
                        SELECT * FROM shipment
                        """)
result = cursor.fetchall()
print(result)


# 4. delete the shipment.id

cursor.execute("""
               DELETE from  shipment where id = 12345
               
               """)


connection.commit()

connection.close()
