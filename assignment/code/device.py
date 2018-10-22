# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 14:19:10 2018

@author: Alasdair
"""

class Device:
    """Class to contain the device details"""
    def __init__(self, deviceType, deviceLocation, deviceID):       
        """Initialise the device data values"""
        self.deviceType = deviceType
        self.deviceLocation = deviceLocation
        self.availability = True
        self.deviceID = deviceID

    def get_device_type(self):
        """Returns the device type"""
        return self.deviceType
    
    def set_device_type(self, deviceType):
        """Sets the device type"""
        self.deviceType = deviceType

    def get_availability(self):
        """Returns the availability"""
        return self.availability    
        
    def set_availability(self, availability):
        """Sets the availability"""
        self.availability = availability
   
    def get_device_location(self):
        """Returns the device location"""
        return self.deviceLocation
    
    def set_device_location(self, deviceLocation):
        """Sets the device location"""
        self.deviceLocation = deviceLocation  
        
    def get_device_id(self):
        """Returns the device ID"""
        return self.deviceID
    
    def set_device_id(self, deviceID):
        """Sets the device ID"""
        self.deviceID = deviceID  
    
   # def checkAvailability(self):
        
    
    def print_details(self):
        """Prints the details of the device"""
        print("Device: " + self.deviceType)
        print("Device ID: " + self.deviceID)
        print("This device is located on Level " + str(self.deviceLocation))
        if self.availability ==True:
            print("This device is currently available")
        else:
            print("This device is currently unavailable")
        
    