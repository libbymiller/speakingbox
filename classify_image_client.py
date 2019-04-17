"""A speaking client for the tensorflow image capture server"""

import signal
import phatbeat
import requests
import os
import sys
import time

# do a request
def takepic(pin):
  #http://docs.python-requests.org/en/master/
  print("Button pressed")
  r = requests.get('http://localhost:8080/explain')
  t = r.text
  arr = t.split(",")
  print(arr[0])
  print("")
  arr1 = arr[0].split("(")
  print(arr1[0])
  print("")
  os.system("/usr/bin/pico2wave -w test.wav '"+arr1[0]+"' | mplayer test.wav")
  time.sleep(1.0)

# run while true
# on button press
def main():
  print("Running main loop")
  os.environ["DISPLAY"] = ":0"
  try:
     while True:
        phatbeat.on(phatbeat.BTN_PLAYPAUSE, takepic)
#        phatbeat.on(phatbeat.BTN_ONOFF, takepic)
        signal.pause()
  except KeyboardInterrupt:
    print("Bye")
    sys.exit()

# main method
if __name__ == "__main__":
    main()


