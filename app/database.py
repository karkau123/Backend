import sqlite3

connection = sqlite3.connect("sqlite.db")
cursor = connection.cursor()




# 1. Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS shipment(
        id INTEGER PRIMARY KEY, 
        content TEXT,
        weight REAL,
        status TEXT  
    )
""")

# 2. Add shipment data
cursor.execute("""
    INSERT INTO shipment
    VALUES(12345, "Palm Trees", 8.5, 'placed')          
""")
connection.commit()

# 3. Read all shipments
cursor = cursor.execute("""
    SELECT * FROM shipment
""")
result = cursor.fetchall()
print(result)

# 4. Delete the shipment by id
cursor.execute("""
    DELETE from shipment where id = 12345
""")
connection.commit()


# 5. update a shipment
id = 12345
status = "in_transit"
cursor.execute("""
    UPDATE shipment
    SET  status = :status
    WHERE id = :id
""" , {"status": status, "id": id})
connection.commit()



# 6. DROP SHIPMENT
cursor.execute("""
    DROP TABLE IF EXISTS shipment
""")
connection.commit()


connection.close()
