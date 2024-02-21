import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='sensordata',
                                         user='root',
                                         password='singh123')

    # mySql_Create_Table_Query = """CREATE TABLE smarthome ( 
    #                          DeviceID varchar(20) NOT NULL,
    #                          Location varchar(50) NOT NULL,
    #                          Temperature varchar (20) NOT NULL,
    #                          Humidity varchar(20) NOT NULL,
    #                          ROOM_1_STATUS varchar (20) NOT NULL,
    #                          TIMSTAMP varchar (50) NOT NULL,
    #                          PRIMARY KEY (DeviceID))
    #                          """
    mySql_Create_Table_Query = """CREATE TABLE diotclassroom ( 
                             SNo int NOT NULL AUTO_INCREMENT,
                             Temperature varchar (20),
                             Humidity varchar(20),
                             TIMESTAMP varchar (50),
                             PRIMARY KEY (SNo)
                             );
                             """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("diotclassroom Table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")