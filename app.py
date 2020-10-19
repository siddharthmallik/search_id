from flask import Flask,render_template,redirect,request,session,flash,url_for,g
import datetime
import sys
import random
import time

import json

import retailMgmt_db

app = Flask(__name__)

app.secret_key = "98app13oct87nxs2020rma6597"

@app.route('/')
def index():
	#get all data from DB
	consumer_info = retailMgmt_db.get_consumerInfo()
	consumerInfo_list = []
	for c in consumer_info:
		consumerInfo_list.append(c)
	return render_template('retailer_mgmt.html', consumerlist = consumerInfo_list)


def setData():
	#Empty List
	consumerRecords = {}
	#request data from UI
	Swo = request.form['swo']
	Date = request.form['date1']
	FirstName = request.form['fName']
	LastName = request.form['lastName']
	Address = request.form['street']
	City = request.form['city']
	State = request.form['state']
	Country = request.form['country']
	Zip = request.form['zip']
	Home = request.form['home']
	Mobile1 = request.form['mobile']
	Mobile2 = request.form['cell']
	Email1 = request.form['email']
	
	
	#set data to the Empty list
	consumerRecords["Swo"]=Swo
	consumerRecords["Date"]=Date
	consumerRecords["FirstName"]=FirstName
	consumerRecords["LastName"]=LastName
	consumerRecords["Address"]=Address
	consumerRecords["City"]=City
	consumerRecords["State"]=State
	consumerRecords["Country"]=Country 
	consumerRecords["Zip"]=Zip
	consumerRecords["Home"]=Home
	consumerRecords["Mobile1"]=Mobile1
	consumerRecords["Mobile2"]=Mobile2
	consumerRecords["Email1"]=Email1 
	
	return consumerRecords


@app.route("/", methods=['POST'])
def update_consumerRecords():	
	consumerRecords = setData()
	#print records in cmd
	print(consumerRecords)
	retailMgmt_db.save_consumer_info(consumerRecords)
	return redirect(url_for('index'))


@app.route("/update", methods=['POST'])
def update_oneConsumer_Records():
	consumerRecords = setData()
	#print records in cmd
	print(consumerRecords)
	#print(request.form['id'])
	#send to db
	consumerid=request.form['id']
	#update_emp = emp_db.get_one_emplyoee_details(empid)
	#print(update_emp)
	retailMgmt_db.update_one_record(consumerid,consumerRecords)
	return redirect(url_for('index'))



@app.route("/edit/<consumer_id>", methods=['POST'])
def edit_record(consumer_id):
	consumerinfo = consumer_id
	consumer_one_record = retailMgmt_db.get_one_consumer_details(consumer_id)
	return render_template('edit_record.html', consumer_list = consumer_one_record)



installers = []
search_results_activated_installer = False




@app.route("/installer", methods=['GET'])
def installerWrapper():
   global installers
   global search_results_activated_installer
   consumerInfo_list = []
   if search_results_activated_installer:
       consumerInfo_list = installers
   else:
       cursor = consumer_db.consumerbasic_info()
       for doc in cursor:
           consumerInfo_list.append(doc)
   search_results_activated_installer = False
   return render_template('retailer_mgmt.html', consumerlist = consumerInfo_list)
@app.route('/installer/searchbyid', methods=['POST'])
def searchInstallerById():
   global installers
   global search_results_activated_installer
   consumerInfo_list = []
   installer_id = request.form['searchbyid']
   consumer_info = retailMgmt_db.get_one_consumer_details(installer_id)
   for doc in consumer_info:
       consumerInfo_list.append(doc)
   print (consumerInfo_list)
   installers = consumerInfo_list
   search_results_activated_installer = True
   return redirect(url_for('installerWrapper'))


@app.route('/installer/searchbyswo', methods=['POST'])
def searchInstallerByswo():
   global installers
   global search_results_activated_installer
   consumerInfo_list = []
   installer_id = request.form['searchbyswo']
   consumer_info = retailMgmt_db.search_installer_by_swo(installer_id)
   for doc in consumer_info:
       consumerInfo_list.append(doc)
   print (consumerInfo_list)
   installers = consumerInfo_list
   search_results_activated_installer = True
   return redirect(url_for('installerWrapper'))


@app.route('/installer/searchbycity', methods=['POST'])
def searchInstallerBycity():
   global installers
   global search_results_activated_installer
   consumerInfo_list = []
   installer_id = request.form['searchbycity']
   consumer_info = retailMgmt_db.search_installer_by_city(installer_id)
   for doc in consumer_info:
       consumerInfo_list.append(doc)
   print (consumerInfo_list)
   installers = consumerInfo_list
   search_results_activated_installer = True
   return redirect(url_for('installerWrapper'))



if(__name__) == '__main__':
	app.run(debug=True)