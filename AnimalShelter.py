  #!/usr/bin/env python
# coding: utf-8

# In[10]:


from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    def __init__(self, username, password):
        
        USER = 'aacuser2'
        PASS = 'password'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31269
        DB = 'AAC'
        COL = 'animals'
        
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # Create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            try:
                self.collection.insert_one(data)  # Insert data
                return True
            except Exception as e:
                raise Exception("Error creating data: " + str(e))
        else:
            raise ValueError("Data was not found")

                
    # Create method to implement the R in CRUD
    def read(self, data):
        if data is not None:
            try:
                result = self.collection.find(data)  # Read data
                return list(result) 
            except Exception as e:
                raise Exception("Error reading data: " + str(e))
        else:
            raise ValueError("Cannot read data")           

    # Create method to implement the U in CRUD
    def update(self, query, updateData):
        if query is not None and updateData is not None:
            try:
                result = self.collection.update_many(query, {'$set': updateData})  
                return result.modified_count
            except Exception as e:
                raise Exception("Error updating data: " + str(e))
        else:
            raise ValueError("Cannot update data")
            
    # Create method to implement the D in CRUD
    def delete(self, data):
        if data is not None:
            try:
                result = self.collection.delete_many(data)  # delete data
                return result.deleted_count 
            except Exception as e:
                raise Exception("Error deleting data: " + str(e))
        else:
            raise ValueError("Cannot delete data")
