import os
import glob
import time
import sys
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
	new_data= str(temp_c)

	
        return temp_c

def printing_module():
	temp = str(read_temp())
	print('At ' + str(time.ctime()) + ' the temperature is ' +  temp + ' degrees.')

	if temp >= 29:
		print('!!!!WARNING: TEMPERATURE IS HIGH!!!')
	else:
		if temp <= 26:
			print('!!!WARNING: TEMPERATURE IS LOW!!!')
		else:
                	time.sleep(0)	
	

def writing_module():
	with open('temperature_log.tsv', 'a') as data_file:
		data_file.write(str(time.ctime()) + '\t' + str(read_temp()) + '\n')
	data_file.close()

def main():
	writing_module()
	printing_module()

while True:
	for i in range(1,10):
		main()		


		#temp = str(read_temp())
		#time_of_measure = str(time.ctime())
		#print('At ' + time_of_measure + ' the temperature is ' + temp + ' degrees.')	
		#time.sleep(1)
		#if temp >= 29:
		#	print('!!!!WARNING: TEMPERATURE IS HIGH!!!')
		#else:
		#	if temp <= 26:
		#		print('!!!WARNING: TEMPERATURE IS LOW!!!')
		#	else:
		#		time.sleep(0)
		#with open('temperature_log.tsv', 'a') as data_file:
		#	data_file.write( time_of_measure + '\t' + temp + '\n')
	
	print "Done now, Bye!!"
	sys.exit(0)
