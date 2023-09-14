from machine import Pin, Timer
import time

led_red= Pin(15,Pin.OUT) #definindo o pino 15 como saida
botao= Pin(16,Pin.IN,Pin.PULL_UP) #definindo o pino 16 como entrada
temporizador = Timer() 

def desliga (timer): #definindo função callback
    global led_red
    led_red.off()
    print("led desligado")

while True:
    if not botao.value():
        temporizador.init(period = 5000, mode = Timer.ONE_SHOT, callback = desliga)
        led_red.on()
        print("led ligado")
        while not botao.value():
            time.sleep_ms(100)