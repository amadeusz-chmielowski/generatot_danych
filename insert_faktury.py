import sys
import dateutil.relativedelta
import random
import numpy

from time import gmtime, strftime
from datetime import datetime

NODRIVERS = 150
NOROADS = 10000
NOCLIENTS = 2500

if __name__ == '__main__':
	t1_size = t2_size = 0
	args = sys.argv[1:]
	iterator = 0
	for arg in args:
		if (arg == '-t1'):
			t1_size = int(args[iterator+1])
		elif (arg == '-t2'):
			t2_size = int(args[iterator+1])
		iterator = iterator + 1
	t2_size = t2_size - t1_size
	
	klienci = open("pesel.txt", "r")
	klienttable = klienci.readlines()
	kierowcy = open("pesel_kierowcy.txt", "r")
	kierowcytable = kierowcy.readlines()
	
	faktury = open("insert/faktury_t1.sql", "w")
	CI_created = 0
	CI_number_act = 1
	time_now = datetime.now()
	time = time_now - dateutil.relativedelta.relativedelta(years=10)
	time_for_driver_main = time
	
	for i in range(0, 2):
		if (i == 1):
			faktury.close()
			faktury = open("insert/faktury_t2.sql", "w")
			t1_size = t2_size
			CI_created = 0
		
		CI_act_year = str(time.year)
		if (t1_size > 0):
			while(True):
				period_time_start_main = time_for_driver_main + dateutil.relativedelta.relativedelta(hours=random.randint(0,3))
				time_for_driver_main = period_time_start_main
				period_time_end_main = period_time_start_main + dateutil.relativedelta.relativedelta(hours=random.randint(3,14))
				drivers_used = numpy.zeros(NODRIVERS)
				for drivers_count in range (0, random.randint(10, int(NODRIVERS/3))):
					driver = random.randint(0, NODRIVERS-1)
					while(drivers_used[driver] == 1):
						driver = random.randint(0, NODRIVERS-1)
					drivers_used[driver] = 1
					
					period_time_start = period_time_start_main + dateutil.relativedelta.relativedelta(minutes=random.randint(0,40))
					time_for_driver = time_for_driver_main + dateutil.relativedelta.relativedelta(minutes=random.randint(0,40))
					period_time_end = period_time_end_main + dateutil.relativedelta.relativedelta(minutes=random.randint(0,40))
					
					while(time_for_driver < period_time_end):
						start_time = time_for_driver + dateutil.relativedelta.relativedelta(minutes=random.randint(1,50)) + dateutil.relativedelta.relativedelta(minutes=random.randint(0,20))
						end_time = start_time + dateutil.relativedelta.relativedelta(minutes=random.randint(8,60))
						klient = klienttable[random.randint(0,NOCLIENTS-1)].replace("\n", "")
						kierowca = kierowcytable[driver].replace("\n", "")
						status_platnosci = random.randint(0,1)
						kilometry = random.randint(100,5000)/100.0
						oplata = kilometry*2 + 6.0
						oplata = float("{0:.2f}".format(oplata))
						trasa = random.randint(0,NOROADS - 1)
						
						if (str(end_time.year) != CI_act_year):
							CI_number_act = 1
							CI_act_year = str(end_time.year)
							break
						CI_number = str(CI_number_act) + '/' + str(end_time.year)
						CI_number_act = CI_number_act + 1
						
						to_insert = "insert into FAKTURY values (" + "\'" + CI_number + "\'" + ", " + "\'" + klient + "\'" + ", " + "\'" + kierowca + "\'" + ", " + "\'" + str(trasa) + "\'" + ", " + "\'" + str(oplata) + "\'" + ", "+ "\'" + str(kilometry) + "\'" + ", " + "\'" + start_time.strftime("%Y-%m-%d %H:%M:%S") + "\'" + ", " + "\'" + end_time.strftime("%Y-%m-%d %H:%M:%S") + "\'" + ", "  + "\'" + str(status_platnosci) + "\'" + ");\n"
						faktury.write(to_insert)
						
						CI_created = CI_created + 1				
						time_for_driver = end_time
						
						if (CI_created >= t1_size):
							break
					if (CI_created >= t1_size):
						break
				if (CI_created >= t1_size):
					break
				time_for_driver_main = period_time_end_main
