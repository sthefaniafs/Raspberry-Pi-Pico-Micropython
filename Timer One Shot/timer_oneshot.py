from machine import Pin, Timer

led_red= Pin(15,Pin.OUT) #definindo o pino 15 como saida
temporizador = Timer() 

def desliga (timer): #definindo função callback
    global led_red
    led_red.off()
    print("led desligado")

print("Iniciando o timer")
temporizador.init(period = 3000, mode = Timer.ONE_SHOT, callback = desliga)
led_red.on()