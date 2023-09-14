from machine import Pin, Timer

led_red= Pin(15,Pin.OUT) #definindo o pino 15 como saida
temporizador = Timer() #definindo timer

def tempo (timer): #definindo função callback
    global led_red
    led_red.toggle()

temporizador.init(period = 1000, mode = Timer.PERIODIC, callback = tempo)

