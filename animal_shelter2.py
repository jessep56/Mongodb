#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon 29 02:56:47 2024

@author: joselaraherna_snhu
"""
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, user, password, host, port, db, collection):
        self.client = MongoClient('mongodb://aacuser:snhu1234@nv-desktop-services.apporto.com:32078/AAC?authSource=AAC')
        self.database = self.client['AAC']
        self.collection = self.database['animals']
        
    def create(self, data):
        if data:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print(f"Error inserting data: {e}")
                return False
        else:
            raise ValueError("Data must be a non-empty dictionary")
            
            
    def read(self, query):
        try:
            results = self.collection.find(query)
            return list(results)
        except Exception as e:
            print(f"Error reading data: {e}")
            return []
        
    def update(self, query, update_data):
        if query and update_data:
            try:
                result = self.collection.update_many(query, {'$set': update_data})
                return result.modified_count
            except Exception as e:
                print(f"Error updating data: {e}")
                return 0
        else:
            raise ValueError("Query and update data must be non-empty dictionaries")
            
    def delete(self, query):
        if query:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print(f"Error deleting data: {e}")
                return 0
        else:
            raise ValueError("Query must be a non-empty dictionary")
            