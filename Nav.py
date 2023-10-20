import time
import serial
serial_port = '/dev/ttyUSB0'  # Replace with your Arduino's serial port
baud_rate = 9600  # Should match the baud rate set on your Arduino

# Open the serial connection
ser = serial.Serial(serial_port, baud_rate)




while True:

    line = ser.readline()

    # Decode the bytes to a string (assuming ASCII encoding)
    decoded_line = line.decode('utf-8').strip()
    values =  decoded_line.split("/n")
    d1 = values[0].strip()
    d2 = values[1].strip()
    ir = values[2].strip()
    if (d1>13 && d2 > 13):
        f()
    if(ir==1):
        time.sleep()
        r()
    if (d1<13 and d2>13 ):

        f()
    if (d1 < 5 and d2 > 8):
        r()

    # if (d1<5 and d2 >13):
    #     r()
    if (d2<5 and d1 >13):
        l()
    if (d1<5 and d2 <5 ):
        break

