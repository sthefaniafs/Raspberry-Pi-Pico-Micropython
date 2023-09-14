from machine import Pin
import utime

led_red= Pin(15,Pin.OUT) #definindo o pino 15 como saida
botao= Pin(16,Pin.IN,Pin.PULL_UP) #definindo o pino 16 como entrada

while True:
    led_red.value(not botao.value())
    utime.sleep_ms(100)
    