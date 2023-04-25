# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 18:25:48 2023

@author: Francisco
"""
import minimalmodbus 
import serial
import time

class F2Gripper():
    def __init__(self,port):
        self.instrument = minimalmodbus.Instrument(port, 9, debug = True)
        self.instrument.serial.port                    
        self.instrument.serial.baudrate = 115200         
        self.instrument.serial.bytesize = 8
        self.instrument.serial.parity   = serial.PARITY_NONE
        self.instrument.serial.stopbits = 1
        self.instrument.serial.timeout  = 0.2
        self.instrument.address                        
        self.instrument.mode = minimalmodbus.MODE_RTU   
        self.instrument.clear_buffers_before_each_transaction = True
        #print(self.instrument)
    def activate_gripper(self):
        self.instrument.write_registers(1000,[256,0,0]) #Activate the gripper
        return 
    def reset_gripper(self):
        self.instrument.write_registers(1000,[0,0,0]) # Reset the gripper
        return 
    def move(self,opening):
        self.instrument.write_registers(1000,[int("00001001"+"00000000",2),
                                   opening,
                                   int(self._intToHex(100)+self._intToHex(100),16)])
        return 
    def _intToHex(self,integer,digits=2):
        exadecimal=hex(integer)[2:]
        exadecimal="0"*(digits-len(exadecimal))+exadecimal
        return exadecimal
class Preassure():
    def __init__(self,port):
        self.arduino = serial.Serial(port=port, baudrate=115200,timeout=.1)
    def set_preasure(self,data):
        try:
            self.arduino.write(bytes(str(data), 'utf-8'))
        except Exception as e:
            print(e)
    def write(self,data):
        self.arduino.write(bytes(str(data), 'utf-8'))
    def close(self):
        self.arduino.close()
