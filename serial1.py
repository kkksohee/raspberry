import serial

SERIALPORT = "/dev/ttyS0"
#SERIALPORT = "/dev/ttyUSB0"
#SERIALPORT = "/dev/ttyAMA0"
BAUDRATE = 115200

ser = serial.Serial(SERIALPORT, BAUDRATE)
ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_NONE #set parity check: no parity
ser.stopbits = serial.STOPBITS_ONE #number of stop bits
ser.timeout = None #block read
ser.xonxoff = False #disable software flow control
ser.rtscts = False #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False #disable hardware (DSR/DTR) flow control
ser.writeTimeout = 0 #timeout for write
