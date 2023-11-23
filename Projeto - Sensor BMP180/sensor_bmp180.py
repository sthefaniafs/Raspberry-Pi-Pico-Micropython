from machine import I2C, Pin
from bmp180 import BMP180
import utime

i2c =I2C(id=0, scl=Pin(1), sda=Pin(0), freq=100000)
bmp180 = BMP180(i2c)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

while True:
    temp = bmp180.temperature
    p = bmp180.pressure
    altitude = bmp180.altitude
    print("Temperatura:", temp, "ºC")
    print ("Pressao:", p,"Pa" )
    print ("Altitude:", altitude, "m")
    utime.sleep(5)

