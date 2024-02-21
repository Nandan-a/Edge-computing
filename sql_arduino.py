import mysql.connector

cnx = mysql.connector.connect(
  user = "root",
  passwd = "root",
  host = "localhost",
  database = "EDGE_Arduino"
)


def insert_data_table(values):
  try:  
    # print(type(temperature))
    
    cur = cnx.cursor()  
    cur.execute("insert into sensor_values values (%s,%s);",values)
    print(cur.rowcount,"record inserted!")    
    cnx.commit()
  except:  
      cnx.rollback()  


# cnx.close()

#mycursor.execute("insert into ")