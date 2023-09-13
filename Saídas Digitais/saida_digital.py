from machine import Pin
import utime

led_red= Pin(15,Pin.OUT)

while True:
    led_red.high() # acende led
    utime.sleep_ms(2000) # por 2 segundos
    led_red.low() # apaga led
    utime.sleep_ms(500) # por meio segundo
