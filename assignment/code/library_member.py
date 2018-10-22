# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 22:58:08 2018

@author: Alasdair
"""

class LibraryMember:
    def __init__(self, name, memberNo):
        """Initialise the electronic resource data values"""
        self.name = name
        self.memberNo = memberNo
        self.resourcesOnLoan = []
        self.messages = []
        
    def set_name(self,name):
        """Sets the library member name"""
        self.name = name
    
    def get_name(self):
        """Returns the Member Name"""
        return self.name   

    def set_member_no(self, memberNo):
        """Sets the Member Number"""
        self.memberNo = memberNo
    
    def get_member_no(self):
        """Returns the Member Number"""
        return self.memberNo 
    
    def add_book(self, newBook):
        """Adds a book to the end of the list of books 
        the library member has currently loaned
        """
        self.resourcesOnLoan.append(newBook)
        
    def print_details(self):    
        """Prints the Details of the Library Member"""
        print("Member Name: " + str(self.getName()))
        print("Author: " + str(self.getMemberNo()))
        for resource in self.resourcesOnLoan:
            resource.printDetails     
    