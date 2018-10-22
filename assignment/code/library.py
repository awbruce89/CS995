# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 23:36:57 2018

@author: Alasdair
"""

from book import Book

class Library:
    def __init__(self):
        self.catalogue = []
        
        
        
        
        
        
        
        
        
        
        
    def isbn_search(self, isbn_search):
        count = 0
        for book in self.catalogue:
            if isinstance(book, Book):
                if book.book.isbn == isbn_search:
                    book.printDetails()
                    count +=1
        if count > 0:
            print(count)
        else:
            print("None")

        
    def author_search(self):
        count = 0
        for author in self.catalogue:
            author.printDetails
            count +=1
        if count > 0:
            print(count)
        else:
            print("None")