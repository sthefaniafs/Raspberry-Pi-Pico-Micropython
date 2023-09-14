import machine
import utime

sensor_chuva= machine.ADC(26)
fator_conversao = 3.3 / (65535)
led_red = machine.Pin(15,machine.Pin.OUT)

while True:
    leitura_chuva = sensor_chuva.read_u16() * fator_conversao
    
    if leitura_chuva > 3:
        print("Não está chovendo")
        led_red.low()
    
    else:
        print("Está chovendo")
        led_red.high()
      
    utime.sleep(2)
