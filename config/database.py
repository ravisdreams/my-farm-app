# import statements

from pymongo import MongoClient

# create database connection

connection = MongoClient("localhost", 27017)
print(connection.list_database_names())
# connection = MongoClient()