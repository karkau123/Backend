import sqlite3
from .schemas import ShipmentCreate

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("sqlite.db")
        self.cur = self.conn.cursor()
        self.create_table("shipment")
        
    def create_table(self, name: str):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS ?(
                id INTEGER PRIMARY KEY, 
                content TEXT,
                weight REAL,
                status TEXT  
            )""",
            (name,)
            )
    
    def create(self ,shipment: ShipmentCreate)->int:
        self.curr.execute("SELECT MAX(id) FROM shipment")
        result = self.curr.fetchone()
        
        new_id = result[0]+1
        
        self.cur.execute("""
                        INSERT INTO shipment
                        VALUES(:id, :content, :weight,:status)
                    """ , {
                         "id": new_id,
                         **shipment.model_dump(),    
                         "status" : "placed"
                    })
        self.conn.commit()
        return new_id
        
        
    def get(self , id : int):
        self.cur = self.cur.execute("""
            SELECT * FROM shipment
            where id = ?
        """, (id,) )
        row = self.cur.fetchall()
        return {
             "id" : row[0],
             "content" : row[1],
             "weight" : row[2],
             "status" : row[3]
        }
        


 







 
 
# 3. Read all shipments
# cursor = cursor.execute("""
#     SELECT * FROM shipment
# """)
# result = cursor.fetchall()
# print(result)

# 4. Delete the shipment by id
# cursor.execute("""
#     DELETE from shipment where id = 12345
# """)
# connection.commit()


# 5. update a shipment
# id = 12345
# status = "in_transit"
# cursor.execute("""
#     UPDATE shipment
#     SET  status = :status
#     WHERE id = :id
# """ , {"status": status, "id": id})
# connection.commit()



# 6. DROP SHIPMENT
# cursor.execute("""
#     DROP TABLE IF EXISTS shipment
# """)
# connection.commit()


# connection.close()
