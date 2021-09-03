import os
import glob
import time

class TemperatureProbe(object):
    # set up the termperature probe
    def __init__(self):
        
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')
        
        base_dir = '/sys/bus/w1/devices/'
        device_folder = glob.glob(base_dir + '28*')[0]
        self.tp = device_folder + '/w1_slave'
    
    # take a raw reading from the probe
    def read_temp_raw(self):
        f = open(self.tp, 'r')
        lines = f.readlines()
        f.close()
        return lines
    
    # if it is a good reading convert to celcius. return error if not valid.
    def read_temp(self):
        lines = self.read_temp_raw()
        try:
            while lines[0].strip()[-3:] != 'YES':
                time.sleep(0.2)
                lines = read_temp_raw()
            equals_pos = lines[1].find('t=')
            if equals_pos != -1:
                temp_string = lines[1][equals_pos+2:]
                temp_c = float(temp_string) / 1000.0
                temp_c = round(temp_c, 1)
                string_temp = str(temp_c)
                return string_temp + "°"
        except:
            return "error"

