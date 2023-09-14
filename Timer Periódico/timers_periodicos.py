from machine import Pin, Timer

led_red= Pin(15,Pin.OUT) #definindo o pino 15 como saida
led_pico= Pin(25,Pin.OUT) #definindo o led da placa como saida
temporizador1 = Timer() 
temporizador2 = Timer() #definindo timers

def tempo1 (timer): #definindo função callback
    global led_red
    led_red.toggle()
    
def tempo2 (timer): #definindo função callback
    global led_pico
    led_pico.toggle()

temporizador1.init(period = 1000, mode = Timer.PERIODIC, callback = tempo1)
temporizador2.init(period = 500, mode = Timer.PERIODIC, callback = tempo2)