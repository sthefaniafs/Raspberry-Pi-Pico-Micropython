from machine import I2C, Pin
from bmp180 import BMP180

i2c =  I2C(scl=Pin(15), sda=Pin(14), freq=100000)   # on esp8266
bmp180 = BMP180(i2c)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

while true:
    temp = bmp180.temperature
    p = bmp180.pressure
    altitude = bmp180.altitude
    print(temp, p, altitude)
