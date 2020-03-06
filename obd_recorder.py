#import platform
from datetime import datetime

import obd_io
import serial
import obd_sensors
import time
import getpass
import obd_api

from obd_utils import scanSerial


class OBD_Recorder():
    """Clase que contra la conexion al OBD y registra los datos obtenido en la base de datos local"""

    def __init__(self, path, log_items):
               
        self.port = None
        self.sensorlist = []
        self.placa = "TEST000"

        localtime = time.localtime(time.time())
        filename = path+"car-"+str(localtime[0])+"-"+str(localtime[1])+"-"+str(
                   localtime[2])+"-"+str(localtime[3])+"-"+str(localtime[4])+"-"+str(localtime[5])+".log"
        self.log_file = open(filename, "w", 128)
        self.log_file.write("placa,reg_date,pids,dtc_status,dtc_ff,fuel_status,load,temp,short_term_fuel_trim_1,long_term_fuel_trim_1,short_term_fuel_trim_2,long_term_fuel_trim_2,fuel_pressure,manifold_pressure,rpm,speed,timing_advance,intake_air_temp,maf,throttle_pos,secondary_air_status,o2_sensor_positions,o211,o212,o213,o214,o221,o222,o223,o224,obd_standard,o2_sensor_position_b,aux_input,engine_time,engine_mil_time,per_driver_torque,per_engine_torque,ref_engine_torque,engine_percent_torque,fuel_tank_level,actual_gear,calculated_gear\n")
        
        filename = path+"car-log"

        for item in log_items:
            self.add_log_item(item)

        self.gear_ratios = [34/13, 39/21, 36/23, 27/20, 26/21, 25/22]
        #log_formatter = logging.Formatter('%(asctime)s.%(msecs).03d,%(message)s', "%H:%M:%S")

    def connect(self):
        portnames = scanSerial()
        #portnames = ['COM10']
        print(portnames)
        for port in portnames:
            self.port = obd_io.OBDPort(port, None, 2, 2)
            if self.port.State == 0:
                self.port.close()
                self.port = None
            else:
                break

        if self.port:
            print("Connected to "+self.port.port.name)

    def is_connected(self):
        return self.port

    def add_log_item(self, item):
        for index, e in enumerate(obd_sensors.SENSORS):
            if(item == e.shortname):
                self.sensorlist.append(index)
                print("Logging item: "+e.name)
                break

    def record_data(self):
        if self.port is None:
            return None

        print("Logging started...")
        
        while 1:

            lat = None
            lng = None

            localtime = datetime.now()
            current_time = str(localtime.hour)+":"+str(localtime.minute) + \
                ":"+str(localtime.second)+"."+str(localtime.microsecond)
            log_string = self.placa+","+str(localtime)
            results = {}
            for index in self.sensorlist:
                (name, value, unit) = self.port.sensor(index)
                log_string = log_string + ","+str(value)
                results[obd_sensors.SENSORS[index].shortname] = value

            gear = self.calculate_gear(results["rpm"], results["speed"])
            if lng == None:
                lng = "0.0"
            if lat == None:
                lat = "0.0"

            log_string = log_string + "," + str(gear) + "," + lng + "," + lat
            #Insertar linea para enviar a API
            datos = log_string.split (",")
            obd_api.send_data(datos[0],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8],
            datos[9],datos[10],datos[11],datos[12],datos[13],datos[14],datos[15],datos[16],datos[17],datos[18],datos[19],
            datos[20],datos[21],datos[22],datos[23],datos[24],datos[25],datos[26],datos[27],datos[28],datos[29],datos[30],
            datos[31],datos[32],datos[33],datos[34],datos[35],datos[36],datos[37],datos[38],datos[39],datos[40],datos[41],
            datos[42],datos[43])
            self.log_file.write(log_string+"\n")

    def calculate_gear(self, rpm, speed):
        if speed == "" or speed == 0:
            return 0
        if rpm == "" or rpm == 0:
            return 0

        rps = rpm/60
        mps = (speed*1.609*1000)/3600

        primary_gear = 85/46  # street triple
        final_drive = 47/16

        tyre_circumference = 1.978  # meters

        current_gear_ratio = (rps*tyre_circumference) / \
            (mps*primary_gear*final_drive)

        # print current_gear_ratio
        gear = min((abs(current_gear_ratio - i), i)
                   for i in self.gear_ratios)[1]
        return gear


username = getpass.getuser()
#logitems = ["rpm", "speed", "throttle_pos", "load", "fuel_status"]
a_logitems = ["pids", "dtc_status", "dtc_ff", "fuel_status", "load", "temp",
"short_term_fuel_trim_1", "long_term_fuel_trim_1", 
"short_term_fuel_trim_2", "long_term_fuel_trim_2", "fuel_pressure",
"manifold_pressure", "rpm", "speed", "timing_advance", "intake_air_temp", "maf",
"throttle_pos", "secondary_air_status", "2nd Air Status", "o2_sensor_positions",
"o211", "o212", "o213", "o214", "o221", "o222", "o223", "o224",
"obd_standard", "o2_sensor_position_b", "aux_input", "engine_time",
"engine_mil_time", "per_driver_torque", "per_engine_torque",
"ref_engine_torque", "engine_percent_torque", "fuel_tank_level", "actual_gear"]

o = OBD_Recorder('/home/' + username + '/pyobd-pi-cmiot/log/', a_logitems)
o.connect()

if not o.is_connected():
    print("Not connected to an OBD device.")
else:
    o.record_data()
