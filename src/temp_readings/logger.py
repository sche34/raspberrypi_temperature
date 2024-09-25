import sys
import os
import time
from vcgencmd import Vcgencmd

def main():
    start_time = time.time()
    fb = open(f"data/readings.txt","a+")
    if os.stat(f"data/readings.txt").st_size == 0:
        fb.write("Elapsed Time (s),Temperature (°C),Clock Speed (MHz),Throttled\n")

    vcgm = Vcgencmd()
    try:
        while True:
            temp = vcgm.measure_temp()
            clock = int(vcgm.measure_clock('arm')/1000000)
            throttled = vcgm.get_throttled()['breakdown']['2']

            timestamp = round(time.time()) # round to nearest second, so that we can save every X seconds
            string = '%.0f,%s,%s,%s\n' % (timestamp,temp,clock,throttled)
            fb.write(string)

            time.sleep(1)
            if timestamp % 5 == 0:
                fb.flush()
    except KeyboardInterrupt:
        fb.close()
        print(f"Exiting... at {time.time()}")
            

if __name__ == '__main__':
    main()