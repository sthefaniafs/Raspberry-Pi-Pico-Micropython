import machine
import utime

sensor_chuva= machine.Pin(14,machine.Pin.IN)
led_red = machine.Pin(15,machine.Pin.OUT)

while True: 
    if sensor_chuva.value():
        print("Não está chovendo")
        led_red.low()
    
    else:
        print("Está chovendo")
        led_red.high()
      
    utime.sleep(2)

