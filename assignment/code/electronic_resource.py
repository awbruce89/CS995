# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 22:11:36 2018

@author: Alasdair
"""

class ElectronicResource:
    def __init__(self, author, title):
        """Initialise the electronic resource data values"""
        self.access_devices = []
        self.author = author
        self.title = title

    def set_author(self, author):
        """Sets the resource author"""
        self.author = author
    
    def get_author(self):
        """Returns the resource author"""
        return self.author

    def set_title(self, title):
        """Sets the resource title"""
        self.title = title
        
    def get_title(self):
        """Returns the resource title"""
        return self.title
    
    def add_access_device(self, device):
        """Adds an accessible device to the list of devices"""
        self.access_devices.append(device)
    
    def print_details(self):
        """Prints the details of the device"""
        print("Title: " + self.title)
        print("Author: " + self.author)    