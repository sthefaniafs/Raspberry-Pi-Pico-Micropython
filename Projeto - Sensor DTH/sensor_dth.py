import machine
import utime
import dht

sensor = dht.DHT11(machine.Pin(4))
vermelho = machine.Pin(13, machine.Pin.OUT) 
azul = machine.Pin(15, machine.Pin.OUT) 
verde = machine.Pin(14, machine.Pin.OUT) 

while True:
    sensor.measure() 
    h = sensor.humidity()
    t = sensor.temperature()
    if (t<35 or h>40):
        vermelho.value(0)
        verde.value(1)
        azul.value(0)
    elif (t==0 or h==20):
        vermelho.value(0)
        verde.value(0)
        azul.value(1)
    else:
        vermelho.value(1)
        verde.value(0)
        azul.value(0)
        
    print("Umidade: ")
    print(h)
    print("Temperatura: ")
    print(t)
    utime.sleep(2)
