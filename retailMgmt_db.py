from pymongo import MongoClient
import datetime
import sys

from bson.objectid import ObjectId

global con
global db
global col

def connect_db():
	global con
	global db
	global col
	# con = MongoClient('mongodb+srv://sundar:sundar@cluster0.dol3j.mongodb.net/retailerManagement_db?retryWrites=true&w=majority')
	# db = con.retailerManagement_db
	# col = db.retailer_info
	con = MongoClient('mongodb+srv://test:test@cluster0.kw4id.mongodb.net/consumer_db?retryWrites=true&w=majority')
	db = con.consumer_db
	col = db.consumerbasic_info


def get_consumerInfo():
	global col
	connect_db()
	consumerInfo_fromDB = col.find({})
	return consumerInfo_fromDB


def save_consumer_info(consumer_info):
	global col
	connect_db()
	col.insert(consumer_info)
	return "saved Successfully"

def get_one_consumer_details(consumer_id):
	global col
	connect_db()
	consumerData_fromDB = col.find({"_id": ObjectId(consumer_id)})
	return consumerData_fromDB

def update_one_record(consumer_id, consumerRecords):
    global col
    connect_db()    
    col.update_one({"_id": ObjectId(consumer_id)}, {'$set' :{'Swo':consumerRecords["Swo"], 'Date':consumerRecords["Date"], 'FirstName':consumerRecords["FirstName"], 'LastName':consumerRecords["LastName"], 'Address':consumerRecords["Address"], 'City':consumerRecords["City"], 'State':consumerRecords["State"], 'Country':consumerRecords["Country"], 'Zip':consumerRecords["Zip"], 'Home':consumerRecords["Home"], 'Mobile1':consumerRecords["Mobile1"], 'Mobile2':consumerRecords["Mobile2"], 'Email1':consumerRecords["Email1"]} })
    return



def search_consumer_by_id(consumer_id):
   global col
   connect_db()
   searched_doc = col.find({'_id':str(consumer_id)})
   return searched_doc


def search_installer_by_swo(installer_id):
   global col
   connect_db()
   searched_doc = col.find({'Swo':str(installer_id)})
   return searched_doc

def search_installer_by_city(installer_id):
   global col
   connect_db()
   searched_doc = col.find({'City':installer_id})
   return searched_doc