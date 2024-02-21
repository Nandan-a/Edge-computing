#pip3 install python-dotenv
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()
"""
Server configuration Details
"""
sql_server_hostname = os.getenv("SQL_SERVER_ADDRESS")
database_user_name = os.getenv("DATABASE_USER_NAME")
database_password = os.getenv("DATABASE_PASSWORD")
mysql_database_name = os.getenv("DATABASE_NAME")

try: 
  # connect method to connect with DB
  sensor_data_db = mysql.connector.connect(
    host=sql_server_hostname,
    user=database_user_name,
    password=database_password,
    database=mysql_database_name
  )
  #get the cursor
  mycursor = sensor_data_db.cursor()

  #table details
  add_data = ("INSERT INTO smarthome "
                "(DeviceID, Location, Temperature, Humidity,ROOM_1_STATUS,TIMSTAMP) "
                "VALUES (%s, %s, %s, %s, %s, %s)")
  deviceid = 'devdiot-01'
  payload = (deviceid, 'Pune', '27c', '87%', 'open', 'Sat, 15 Jul 2023 10:51:11')
  mycursor.execute(add_data, payload)

  #commit the record
  mycursor = sensor_data_db.commit()

  #debug

  print(mycursor.rowcount, "record inserted.")
except Exception as e:
  print(e)
