from datetime import datetime
import os
import time
from vcgencmd import Vcgencmd

def main():
    fb = open(f"data/readings.txt","a+")
    if os.stat(f"data/readings.txt").st_size == 0:
        fb.write("Timestamp,Temperature (°C),Clock Speed (MHz),Throttled\n")
        fb.flush()

    vcgm = Vcgencmd()
    try:
        while True:
            temp = vcgm.measure_temp()
            clock = int(vcgm.measure_clock('arm')/1000000)
            throttled = vcgm.get_throttled()['breakdown']['2']

            timestamp = datetime.now()
            string = '%s,%s,%s,%s\n' % (timestamp,temp,clock,throttled)
            fb.write(string)

            time.sleep(1)
            if timestamp.second % 5 == 0:
                fb.flush()
            
            if timestamp.second % 59 == 0:
                print(f"Timestamp: {timestamp}, Temp: {temp}, Clock: {clock}, Throttled: {throttled}")
    except KeyboardInterrupt:
        fb.close()
        print(f"Exiting... at {datetime.now()}")

if __name__ == '__main__':
    main()