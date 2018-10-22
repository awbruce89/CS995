# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 23:11:29 2018

@author: Alasdair
"""

class Book:
    """Class to contain the book details"""
    def __init__(self, author, title, no_of_pages, isbn, damages):
        """Initialise the book data values"""
        self.author = author
        self.title = title
        self.no_of_pages = no_of_pages
        self.availability = False
        self.isbn = isbn
        self.library_member = None
        self.damages = damages

    def set_availability(self, availability):
        """Sets the availability of the book"""
        self.availability = availability

    def get_availability(self):
        """Returns the availability of the book"""
        return self.availability            
        
    def set_library_member(self, library_member):
        """Sets the member currently in possession of the book"""
        self.library_member = library_member
    
    def get_library_member(self):
        """Returns the member currently in possession of the book"""
        return self.library_member
    
    def set_author(self, author):
        """Sets the book author"""
        self.author = author
    
    def get_author(self):
        """Returns the book author"""
        return self.author

    def set_title(self, title):
        """Sets the book title"""
        self.title = title
        
    def get_title(self):
        """Returns the book title"""
        return self.title
    
    def set_pages(self, no_of_pages):
        """Sets the number of pages in the book"""
        self.no_of_pages = no_of_pages
        
    def get_pages(self):
        """Returns the number of pages in the book"""
        return self.no_of_pages

    def set_isbn(self, isbn):
        """Sets the ISBN of the book"""
        self.isbn = isbn
        
    def get_isbn(self):
        """Returns the ISBN of the book"""
        return self.isbn

    def set_damages(self, damages):
        """Adds new damages to the existing set of damages"""
        self.damages = self.damages + "\n" + damages
    
    def get_damages(self):
        """Returns the books damages"""
        return self.damages
   
    def check_availability(self):
        """Checks for the availability of the book"""
        if self.library_member == None:
            return True
        else:
            return False
    
    def print_details(self):
        """Prints the Details of the Device"""
        print("Title: " + (self.getTitle()))
        print("Author: " + (self.getAuthor()))
        print("Number of Pages: " + str(self.no_of_pages))
        print("Current Damage: " + self.damages)
        print("ISBN: " + self.isbn )
        if self.check_availability() == True:
            print("Book is available")
        else:
            print("Book is unavailable")


"""DO I NEED ANOTHER METHOD TO PRINT BOOK DETAILS FOR A MEMBER?"""


def test():
    book1 = Book("Brandon Sanderson", "Mistborn", 500, "111111111", "Small tear in book jacket")
    book1.printDetails()
    book1.setDamages("Page corners folded")
    book1.printDetails()