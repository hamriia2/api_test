# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 06:36:53 2019

@author: 406760
"""
import pandas as pd

from flask import Flask, jsonify, request


app = Flask(__name__)




books =[{
         "Name":"Chacha Chaudhari and Sabu",
         "Price": 200,
         "isbn": 90001
        
        },
        {
         "Name":"Nagraj and Sabu",
         "Price": 300,
         "isbn": 90002        

                
         }

        ]

def validBookObject(bookObject):
    if ("Name" in bookObject and "Price" in bookObject and "isbn" in bookObject):
        return True
    else:
        return False

@app.route('/books')
def hello_world():
    return jsonify({"Books": books})

@app.route('/books', methods=['POST'])
def add_book():
    rd=request.get_json()
    if(validBookObject(rd)):
        books.insert(0,rd)
        return "True"
    else:
        return "False"
    
    

#@app.route('/books', methods=['POST'])
#def add_book():
#    req=request.get_json()
#    if(validBookObject(req)):
#        books.insert(0,req)
#        return True
#    else:
#        return False
    #return jsonify(request.get_json())

@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value={}
    for book in books:
        if book["isbn"]==isbn:
            return_value={"Name":book["Name"], "Price":book["Price"]}
    
    return jsonify(return_value)

app.run(port=5000,debug = True)
