import mysql.connector

cnx = mysql.connector.connect(
  user = "root",
  passwd = "root",
  host = "localhost",
  database = "EDGE"
)


def insert_data_table(temperature_data,humidity_data,door_status_data,window_status_data):
  try:  
    print(type(temperature_data))
    
    cur = cnx.cursor()  
    cur.execute("insert into sensor_values values (%s,%s,%s,%s);",(temperature_data,humidity_data,door_status_data,window_status_data)) 
    print(cur.rowcount,"record inserted!")    
    cnx.commit()
  except:  
      cnx.rollback()  


cnx.close()

#mycursor.execute("insert into ")