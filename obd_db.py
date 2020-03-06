import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return conn

def insert_data(conn, data):
   """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
 
    sql = '''INSERT INTO datos (placa,reg_date,pids,dtc_status,dtc_ff
           ,fuel_status,car_load,temp
           ,short_term_fuel_trim_1
           ,long_term_fuel_trim_1
           ,short_term_fuel_trim_2
           ,long_term_fuel_trim_2
           ,fuel_pressure
           ,manifold_pressure
           ,rpm
           ,speed
           ,timing_advance
           ,intake_air_temp
           ,maf
           ,throttle_pos
           ,secondary_air_status
           ,o2_sensor_positions
           ,o211
           ,o212
           ,o213
           ,o214
           ,o221
           ,o222
           ,o223
           ,o224
           ,obd_standard
           ,o2_sensor_position_b
           ,aux_input
           ,engine_time
           ,engine_mil_time
           ,per_driver_torque
           ,per_engine_torque
           ,ref_engine_torque
           ,longitude
           ,latitude
           ,is_sync)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid

def create_table(conn):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """

    SQL_TABLE_DATOS = """CREATE TABLE IF NOT EXISTS datos (
                        idx int PRIMARY KEY,
                        placa varchar(10) NOT NULL,
                        reg_date datetime NOT NULL,
                        pids varchar(100) NOT NULL,
                        dtc_status varchar(50) NOT NULL,
                        dtc_ff varchar(50) NOT NULL,
                        fuel_status varchar(50) NOT NULL,
                        car_load varchar(50) NOT NULL,
                        temp varchar(50) NOT NULL,
                        short_term_fuel_trim_1 varchar(50) NOT NULL,
                        long_term_fuel_trim_1 varchar(50) NOT NULL,
                        short_term_fuel_trim_2 varchar(50) NOT NULL,
                        long_term_fuel_trim_2 varchar(50) NOT NULL,
                        fuel_pressure varchar(50) NOT NULL,
                        manifold_pressure varchar(50) NOT NULL,
                        rpm varchar(50) NOT NULL,
                        speed varchar(50) NOT NULL,
                        timing_advance varchar(50) NOT NULL,
                        intake_air_temp varchar(50) NOT NULL,
                        maf varchar(50) NOT NULL,
                        throttle_pos varchar(50) NOT NULL,
                        secondary_air_status varchar(50) NOT NULL,
                        o2_sensor_positions varchar(50) NOT NULL,
                        o211 varchar(50) NOT NULL,
                        o212 varchar(50) NOT NULL,
                        o213 varchar(50) NOT NULL,
                        o214 varchar(50) NOT NULL,
                        o221 varchar(50) NOT NULL,
                        o222 varchar(50) NOT NULL,
                        o223 varchar(50) NOT NULL,
                        o224 varchar(50) NOT NULL,
                        obd_standard varchar(50) NOT NULL,
                        o2_sensor_position_b varchar(50) NOT NULL,
                        aux_input varchar(50) NOT NULL,
                        engine_time varchar(50) NOT NULL,
                        engine_mil_time varchar(50) NOT NULL,
                        per_driver_torque varchar(50) NOT NULL,
                        per_engine_torque varchar(50) NOT NULL,
                        ref_engine_torque varchar(50) NOT NULL,
                        longitude varchar(50) NOT NULL,
                        latitude varchar(50) NOT NULL,
                        is_sync bit NOT NULL,
                    );"""
    try:
        c = conn.cursor()
        c.execute(SQL_TABLE_DATOS)
    except Error as e:
        print(e)