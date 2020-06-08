import serial, time, os
from Adafruit_IO import Client
aio = Client('alexleoleo', 'aio_tIkm200lkzJKnPlPI6YwqLrkxnU1')
 
ser = serial.Serial ('/dev/ttyUSB0')

print(os.getenv('PY_CLIENT', ''))
print(os.getenv('PY_KEY', ''))
 
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