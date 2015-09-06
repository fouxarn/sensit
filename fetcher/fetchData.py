# -*- coding: utf-8 -*-
import smbus
import time
import requests
import threading
bus = smbus.SMBus(1)

address = 0x04

def writeSensor(value):
        bus.write_byte(address, int(value))
        return -1

def readSensor(value):
            #var = input('Enter 1 – 9:')
            #print ("RPI: I will send " + var)
            writeSensor(int(value))
            #print ("RPI: Hi Arduino, I sent you " + var)

            #forceStrSize = 4
            #data = ''
            #for _ in range(0, forceStrSize):
            #    data += chr(bus.read_byte(address))

            #longData = int.from_bytes(data, byteorder='little')
            #data = data.encode('utf-8')
            #print ("Data: " + data.decode())
            sensorData = bus.read_byte(address)
            #print("Sensordata: " + str(sensorData))
            #print()
            payload = {'plate_id':int(value+1),'weight':sensorData}
            requests.post('http://localhost:5000/update', data=payload)

def readSensors():
    threading.Timer(5.0, readSensors).start()
    readSensor(0)
    readSensor(1)

readSensors()
