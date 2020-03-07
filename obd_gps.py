import serial
import pynmea2
import time
 
def streamGPS(serial_port, serial_speed):
    """Streams into screen the gps fixed locations"""
    port = serial_port #/dev/ttyUSB1
    ser = serial.Serial(port, serial_speed, timeout=0) #9600

    streamreader = pynmea2.NMEAStreamReader()

    while True:
        data = ser.read()
        for msg in streamreader.next(data):
            for line in str(msg).split('\n') :
                if line.startswith( '$GPGGA' ) :
                    msg2 = pynmea2.parse(line)
                    print("Latitude: " + str(msg2.latitude) + " Longitud:" + str(msg2.longitude) + " Altitude: " + str(msg2.altitude))

    
    ser.close()

def getGPS(serial_port, serial_speed):
    """Reads GPS fixed location from NMEA port"""
    port = serial_port #/dev/ttyUSB1
    ser = serial.Serial(port, serial_speed, timeout=0) #9600

    streamreader = pynmea2.NMEAStreamReader()

    while True:
        data = ser.read()
        for msg in streamreader.next(data):
            for line in str(msg).split('\n') :
                if line.startswith( '$GPGGA' ) :
                    msg2 = pynmea2.parse(line)
                    ser.close()
                    obj = {"lat": msg2.latitude, "lng": msg2.longitude, "alt": msg2.altitude }
                    return obj
    ser.close()

    
    
    

