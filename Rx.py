mport serial
import time
#SERIALPORT = "/dev/ttyS0"
SERIALPORT = "/dev/ttyUSB0"
#SERIALPORT = "/dev/ttyAMA0"
BAUDRATE = 115200
ser = serial.Serial(SERIALPORT, BAUDRATE)
ser.bytesize = serial.EIGHTBITS
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.timeout = None
ser.xonxoff = False
ser.rtscts = False
ser.dsrdtr = False
ser.writeTimeout = 0
print ("Starting Up Serial Monitor")

try:
  ser.open()
except Exception as e:
  print ("Exception: Opening serial port: " + str(e))
#finally:
# ser.close()
if ser.isOpen():
  while 1:
    ser.flushOutput()
    ser_bytes = ser.readline()
    decoded_bytes = (ser_bytes.decode("utf-8"))
    
    print('Receiving’)
    print(type(decoded_bytes))
    print('Rx Data: '+ decoded_bytes)
    time.sleep(0.5)
    # programming..
else:
  print ("Cannot open serial port.")

