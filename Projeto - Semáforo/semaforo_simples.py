from machine import Pin
import utime

led_red= Pin(15,Pin.OUT) #definindo o pino 15 como saida
led_yellow= Pin(14,Pin.OUT) #definindo o pino 14 como saida
led_green= Pin(13,Pin.OUT) #definindo o pino 13 como saida

while True:
    led_red.value(1)
    utime.sleep(5) #led vermelho fica aceso por 5s
    led_red.value(0) #led vermelho apaga
    led_green.value(1) 
    utime.sleep(5) #led verde fica aceso por 5s
    led_green.value(0) #led verde apaga
    led_yellow.value(1) 
    utime.sleep(3) #led amarelo fica aceso por 3s
    led_yellow.value(0) #led amarelo apaga