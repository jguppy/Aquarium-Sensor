import os
import glob
import time
import sys
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'



#device_folder = glob.glob(base_dir + '28*')[0]
#device_file = device_folder + '/w1_slave'

device_folder_RT = glob.glob(base_dir + '28-00000829038a')[0]
device_file_RT = device_folder_RT + '/w1_slave'

device_folder_TT = glob.glob(base_dir + '28-0000082969bf')[0]
device_file_TT = device_folder_TT + '/w1_slave'

device_folder_ST = glob.glob(base_dir + '28-00000829ab3e')[0]
device_file_ST = device_folder_ST + '/w1_slave'
 
#RT=28-00000829038a
#TT=28-0000082969bf
#ST=28-00000829ab3e

def read_temp_raw_RT():
    f = open(device_file_RT, 'r')
    lines_RT = f.readlines()
    f.close()

    return lines_RT

def read_temp_raw_TT():
    f_2 = open(device_file_TT, 'r')
    lines_TT = f_2.readlines()
    f_2.close()

    return lines_TT

def read_temp_raw_ST():
    f_3 = open(device_file_ST, 'r')
    lines_ST = f_3.readlines()
    f_3.close()	
    
    return lines_ST
 
def read_temp_RT():
    lines_RT = read_temp_raw_RT()
    while lines_RT[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines_RT = read_temp_raw_RT()
    equals_pos = lines_RT[1].find('t=')
    if equals_pos != -1:
        temp_string = lines_RT[1][equals_pos+2:]
        temp_RT = float(temp_string) / 1000.0
	new_data= str(temp_RT)

    return temp_RT

def read_temp_TT():
    lines_TT = read_temp_raw_TT()
    while lines_TT[0].strip()[-3:] !='YES':
        time.sleep(0.2)
	lines_TT = read_temp_raw_TT()
    equals_pos_TT = lines_TT[1].find('t=')
    if equals_pos_TT != -1:
        temp_string_TT = lines_TT[1][equals_pos_TT+2:]
	temp_TT = float(temp_string_TT) / 1000.0
	new_data_TT = str(temp_TT)

    return temp_TT

def read_temp_ST():
   lines_ST = read_temp_raw_ST()
   while lines_ST[0].strip()[-3:] !='YES':
       time.sleep(0.2)
       lines_ST = read_temp_raw_ST()
   equals_pos_ST = lines_ST[1].find('t=')
   if equals_pos_ST != -1:
       temp_string_ST = lines_ST[1][equals_pos_ST+2:]
       temp_ST = float(temp_string_ST) / 1000.0
       new_data_ST = str(temp_ST)
   
   return temp_ST

def printing_module():
	temp_RT = str(read_temp_RT())
	temp_TT = str(read_temp_TT())
	temp_ST = str(read_temp_ST())
 
	print('At ' + str(time.ctime()) +':' + '\n'  + 'The room temperature is ' +  temp_RT + ' degrees.' + '\n' + 'The tank temperature is ' + temp_TT + ' degrees.' + '\n' + 'The sump temperature is ' + temp_ST + ' degrees.')

	#if temp >= 29:
	#	print('!!!!WARNING: TEMPERATURE IS HIGH!!!')
	#else:
	#	if temp <= 26:
	#		print('!!!WARNING: TEMPERATURE IS LOW!!!')
	#	else:
        #        	time.sleep(0)	
	

def writing_module():
	with open('temperature_log.tsv', 'a') as data_file:
		data_file.write(str(time.ctime()) + '\t' + str(read_temp_RT()) + '\t' + str(read_temp_TT()) + '\t' + str(read_temp_ST()) + '\t' + '\n')
	data_file.close()

def main():
	writing_module()
	printing_module()

while True:
	for i in range(1,10):
		main()		



	print "Done now, Bye!!"
	sys.exit(0)
