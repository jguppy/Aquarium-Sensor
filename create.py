import csv
import sys

## ask for file details
print("Creating new file")
name = input("Enter the name of the file:")
extension = input("Enter the extension type:")
file_name= name+"." +extension

	## need to figure out how to call variables between functions
	## return function doesnt seem to be working for some reason

def create():
	## creates the file intially
	## and also stores the file name for later use

	new_file=open(file_name,'a')

	print("New file created")

	new_file.close()

def writer_module():
	## this calls the create module
	## and then asks for new data to be entered
	## it is then added to the bottum of the created/existing tsv file

	new_data = input('Enter you data seperated by tabs:')
	new = str(new_data)
	print("Writing data to file")

	with open(file_name,'a') as updated_file:
		updated_file.write(new+'\n')

def adding_more():
	new_data = input('Enter you data seperated by tabs:')
	new= str(new_data)
	print("Adding extra data to file")

	with open(file_name,'a') as second_file:
		second_file.write(new+'\n')

def do_you_want_more_data():

	answer = input("Do you want to add more data? [Y/N]")
	if answer=="Y":
		print("Ok lets add some more then...")
		adding_more_data = adding_more()
		more_data_again = more_data()
	elif answer=="N":
		print("Ok. bye then")
		sys.exit(0)
	else:
		print("Please answer Y or N")

def main():
	create()
	writer_module()
	do_you_want_more_data()

main()


