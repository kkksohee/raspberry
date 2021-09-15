import serial

ser = serial.Serial(
  port= '/dev/ttyS0',
  baudrate = 115200, # 9600, 115200
  parity= serial.PARITY_NONE,
  stopbits= serial.STOPBITS_ONE,
  bytesize= serial.EIGHTBITS,
  timeout=1,
  xonxoff = False, 
  rtscts = False, 
  dsrdtr = False, 
  writeTimeout = 0
)
