from machine import Pin
import utime
import _thread


led_red= Pin(15,Pin.OUT) #definindo o pino 15 como saida
led_yellow= Pin(14,Pin.OUT) #definindo o pino 14 como saida
led_green= Pin(13,Pin.OUT) #definindo o pino 13 como saida
button = Pin(16, Pin.IN, Pin.PULL_DOWN) #definindo o pino 11 como entrada
buzzer = Pin(12, Pin.OUT) #definindo o pino 16 como saida

global button_pressed
button_pressed = False

def button_reader_thread(): #definindo o novo valor de button_pressed
    global button_pressed
    while True:
        if button.value() == 1:
            button_pressed = True
        utime.sleep(0.01)
        
_thread.start_new_thread(button_reader_thread, ())

while True:
    if button_pressed == True:
        led_red.value(1)
        for i in range(10): #definindo período de toque do buzzer
            buzzer.value(1)
            utime.sleep(0.2)
            buzzer.value(0)
            utime.sleep(0.2)
        global button_pressed
        button_pressed = False
        
    led_red.value(1)
    utime.sleep(5) #led vermelho fica aceso por 5s
    led_red.value(0) #led vermelho apaga
    led_green.value(1) 
    utime.sleep(5) #led verde fica aceso por 5s
    led_green.value(0) #led verde apaga
    led_yellow.value(1) 
    utime.sleep(3) #led amarelo fica aceso por 3s
    led_yellow.value(0) #led amarelo apaga
