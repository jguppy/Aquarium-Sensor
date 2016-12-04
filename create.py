import csv
import sys
import datetime
import json

def create():
	print("Creating new file")
	name = input('Enter the name of the file:')
	extension = input("Enter the extension type:")

	try:
		file_name=name+"."+extension
		return file_name
		new_file=open(file_name,'a')

		print("New file created")
		
		#return file_name
		new_file.close()

	except ValueError:
		print("Error occured")

def writer_module():
	file_name = create()
	
	new_data = input('Enter you data seperated by tabs:')
	new = str(new_data)
	print("Writing data to file")

	with open(file_name,'a') as updated_file:
		updated_file.write(new+'\n')
		#read_data = updated_file.read()
	sys.exit(0)


writer_module()

#create()
#writer_module(create)


