import machine
import utime

led_red= machine.Pin(16,machine.Pin.OUT) #definindo o pino 15 como saida
ldr= machine.ADC(26)

fator_conversao = 3.3 / (65535)


while True:
    leitura_LDR = ldr.read_u16() * fator_conversao
    utime.sleep(2)
    print(leitura_LDR)
    if (leitura_LDR < 1):
       led_red.value(1)
    else:
        led_red.value(0)

