# import pyserial and adafruit-io
import serial, time, os
from Adafruit_IO import Client

# read the env 
pySerial = os.getenv('PY_SERIAL', '')
pyClient = os.getenv('PY_CLIENT', '')
pyKey = os.getenv('PY_KEY', '')

print("SERIAL-PORT: " + pySerial)
print("ADAFRUIT-CLIENT: " + pyClient)
print("ADAFRUIT-KEY: " + pyKey)

# init adafruit-io and serial 
aio = Client(pyClient, pyKey)
ser = serial.Serial (pySerial)

# infinite loop 
while True:
    data = []
    for index in range (0,10):
           datum = ser.read()
           data.append(datum)

    pmtwofive = int.from_bytes(b''.join(data[2:4]), byteorder='little') / 10
    print(pmtwofive)
    aio.send('melzotwofive', pmtwofive)
    pmten = int.from_bytes(b''.join(data[4:6]), byteorder='little') / 10
    aio.send('melzoten',pmten)
    print(pmten)
    time.sleep(10)