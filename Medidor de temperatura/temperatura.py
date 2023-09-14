import machine
import utime

sensor_temp = machine.ADC(4)
fator_conversao = 3.3 / (65535)

while True:
    leitura_ADC  = sensor_temp.read_u16() * fator_conversao
    temperatura = 27 - (leitura_ADC  - 0.706)/0.001721
    print(temperatura)
    utime.sleep(2)