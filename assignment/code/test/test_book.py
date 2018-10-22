# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 16:03:37 2018

@author: Alasdair
"""

import unittest
from code.book import Book
#from code.member import Member


class TestStudent(unittest.TestCase):
    """A test class for Book the class"""
    def setUp(self):
        """Set up book objects to test"""
        self.book1 = Book("Brandon Sanderson", "Mistborn", 500, "111111111", "Small tear in book jacket")
                
    def test_book_creation(self):
        """A test for student creation and getter methods"""
        #self.book1 = Book("Brandon Sanderson", "Mistborn", 500, "111111111", "Small tear in book jacket")
        self.assertEqual(self.book1.get_author(), "Brandon Sanderson")
        self.assertEqual(self.book1.get_title(), "Mistborn")
        self.assertEqual(self.book1.get_pages(), 500)
        self.assertEqual(self.book1.get_isbn(), "111111111")
        self.assertEqual(self.book1.get_damages(), "Small tear in book jacket")
        self.assertEqual(self.book1.library_member(), "Small tear in book jacket")
        self.assertEqual(self.book1.get_availability(), False)
        

    def test_set_author(self):
        """A test for setting author name"""
        self.book1.set_author("J R R Tolkien")
        self.assertEqual(self.book1.author, "J R R Tolkien")
        
    def test_set_title(self):
        """A test for setting book title"""
        self.book1.set_title("Lord of the Rings")
        self.assertEqual(self.book1.title, "Lord of the Rings")
        
    def test_set_pages(self):
        """A test for setting book pages"""
        self.book1.set_pages(1000)
        self.assertEqual(self.book1.no_of_pages, 1000)

    def test_set_isbn(self):
        """A test for setting book ISBN"""
        self.book1.set_isbn("123456789")
        self.assertEqual(self.book1.isbn, "123456789")
        
    def test_set_damages(self):
        """A test for setting book damages"""
        self.book1.set_damages("Torn contents page")
        self.assertEqual(self.book1.damages, "Small tear in book jacket\nTorn contents page")

    def test_set_availability(self):
        """A test for setting book damages"""
        self.book1.set_availability(True)
        self.assertEqual(self.book1.availability, True)



    
"""NEED TO TEST LIBRARY MEMBER SETTER!!!"""




    def test_check_availability_false(self):
        """A test for checking book availability"""
        self.assertEqual(self.book1.)

if __name__ == '__main__':
    unittest.main()